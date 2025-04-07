"""
Periodic Table Explorer

An interactive application to explore chemical elements with multilingual support
for English, Portuguese, and Norwegian. Displays detailed information about
each element including properties, discovery, and color-coded categories.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json

class PeriodicTableExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Periodic Table Explorer")
        self.root.geometry("900x700")
        
        # Define element colors by category
        self.element_colors = {
            "alkali metal": "#ff6666",           # Red
            "alkaline earth metal": "#ffdead",    # Peach
            "transition metal": "#ffc0c0",        # Pink
            "post-transition metal": "#cccccc",   # Gray
            "metalloid": "#cccc99",               # Khaki
            "nonmetal": "#a0ffa0",                # Light green
            "halogen": "#ffff99",                 # Light yellow
            "noble gas": "#c0ffff",               # Light cyan
            "lanthanide": "#ffbfff",              # Light purple
            "actinide": "#ff99cc"                 # Light pink
        }
        
        # Load element data from the separate module
        self.elements = self.load_element_data()
        
        # Create GUI
        self.create_widgets()
    
    def load_element_data(self):
        """
        Load element data from the element_data module.
        Falls back to a minimal dataset if the module is not found.
        """
        try:
            # Try to import from the element_data module
            from element_data import elements_data
            return elements_data
        except ImportError:
            # Fallback to minimal data if the import fails
            print("Warning: element_data.py not found, using minimal dataset")
            return {
                "1": {
                    "symbol": "H",
                    "names": {
                        "en": "Hydrogen",
                        "pt": "Hidrogênio",
                        "no": "Hydrogen"
                    },
                    "atomic_number": 1,
                    "atomic_mass": 1.008,
                    "category": "nonmetal",
                    "electron_configuration": "1s¹",
                    "electronegativity": 2.20,
                    "density": 0.00008988,
                    "melting_point": 14.01,
                    "boiling_point": 20.28,
                    "discovered_by": "Henry Cavendish",
                    "year_discovered": 1766
                },
                # Add a few more elements to allow the program to run with minimal data
                "2": {
                    "symbol": "He",
                    "names": {
                        "en": "Helium",
                        "pt": "Hélio",
                        "no": "Helium"
                    },
                    "atomic_number": 2,
                    "atomic_mass": 4.0026,
                    "category": "noble gas",
                    "electron_configuration": "1s²",
                    "electronegativity": None,
                    "density": 0.0001785,
                    "melting_point": 0.95,
                    "boiling_point": 4.22,
                    "discovered_by": "Pierre Janssen, Norman Lockyer",
                    "year_discovered": 1868
                }
            }
    
    def create_widgets(self):
        """
        Create all GUI widgets and layout for the application.
        """
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create language selection
        language_frame = ttk.LabelFrame(main_frame, text="Language", padding="5")
        language_frame.pack(fill=tk.X, pady=5)
        
        self.language_var = tk.StringVar(value="en")
        languages = [
            ("English", "en"),
            ("Portuguese", "pt"),
            ("Norwegian", "no")
        ]
        
        for i, (text, value) in enumerate(languages):
            ttk.Radiobutton(
                language_frame, 
                text=text, 
                value=value, 
                variable=self.language_var,
                command=self.update_element_list
            ).grid(row=0, column=i, padx=10)
        
        # Create search frame
        search_frame = ttk.Frame(main_frame)
        search_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(search_frame, text="Search:").pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.update_element_list())
        ttk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side=tk.LEFT, padx=5)
        
        # Create element selection frame
        selection_frame = ttk.Frame(main_frame)
        selection_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Element listbox
        list_frame = ttk.LabelFrame(selection_frame, text="Elements", padding="5")
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.element_listbox = tk.Listbox(list_frame, width=25, height=20)
        self.element_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.element_listbox.bind("<<ListboxSelect>>", self.show_element_details)
        
        # Scrollbar for listbox
        listbox_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.element_listbox.yview)
        listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.element_listbox.config(yscrollcommand=listbox_scrollbar.set)
        
        # Element details frame
        details_frame = ttk.LabelFrame(selection_frame, text="Element Details", padding="5")
        details_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Element color display
        self.color_frame = ttk.Frame(details_frame, width=80, height=80, style="Color.TFrame")
        self.color_frame.pack(pady=5)
        
        # Element information
        info_frame = ttk.Frame(details_frame)
        info_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create text widget for details
        self.details_text = tk.Text(info_frame, wrap=tk.WORD, width=40, height=20)
        self.details_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.details_text.config(state=tk.DISABLED)
        
        # Scrollbar for details
        details_scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=self.details_text.yview)
        details_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.details_text.config(yscrollcommand=details_scrollbar.set)
        
        # Export button
        ttk.Button(main_frame, text="Export All Data as JSON", command=self.export_data).pack(pady=10)
        
        # Populate the element list
        self.update_element_list()
    
    def update_element_list(self):
        """
        Update the element listbox based on current language and search filter.
        """
        self.element_listbox.delete(0, tk.END)
        language = self.language_var.get()
        search_text = self.search_var.get().lower()
        
        for element_id, element_data in sorted(self.elements.items(), key=lambda x: int(x[0])):
            element_name = element_data["names"][language]
            element_symbol = element_data["symbol"]
            display_text = f"{element_data['atomic_number']}. {element_symbol} - {element_name}"
            
            if search_text in display_text.lower() or search_text in str(element_data["atomic_number"]):
                self.element_listbox.insert(tk.END, display_text)
    
    def show_element_details(self, event):
        """
        Display detailed information about the selected element.
        """
        selection = self.element_listbox.curselection()
        if not selection:
            return
        
        selected_display = self.element_listbox.get(selection[0])
        atomic_number = int(selected_display.split(".")[0])
        
        # Find the element data
        element_data = None
        for element_id, data in self.elements.items():
            if data["atomic_number"] == atomic_number:
                element_data = data
                break
        
        if not element_data:
            return
            
        # Update color frame
        color = self.element_colors.get(element_data["category"], "#ffffff")
        self.root.style = ttk.Style()
        self.root.style.configure("Color.TFrame", background=color)
        
        # Update details text
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)
        
        language = self.language_var.get()
        
        # Create detailed information text
        details = [
            f"Symbol: {element_data['symbol']}",
            f"Names:",
            f"  English: {element_data['names']['en']}",
            f"  Portuguese: {element_data['names']['pt']}",
            f"  Norwegian: {element_data['names']['no']}",
            f"Atomic Number: {element_data['atomic_number']}",
            f"Atomic Mass: {element_data['atomic_mass']} u",
            f"Category: {element_data['category'].title()}",
            f"Electron Configuration: {element_data['electron_configuration']}",
        ]
        
        # Handle potential None for electronegativity
        if element_data['electronegativity']:
            details.append(f"Electronegativity: {element_data['electronegativity']}")
        else:
            details.append(f"Electronegativity: Not applicable")
            
        details.extend([
            f"Density: {element_data['density']} g/cm³",
            f"Melting Point: {element_data['melting_point']} K",
            f"Boiling Point: {element_data['boiling_point']} K",
            f"Discovered by: {element_data['discovered_by']}",
            f"Year discovered: {element_data['year_discovered'] if element_data['year_discovered'] else 'Ancient times'}"
        ])
        
        self.details_text.insert(tk.END, "\n".join(details))
        self.details_text.config(state=tk.DISABLED)
    
    def export_data(self):
        """
        Export all element data to a JSON file.
        """
        try:
            with open("periodic_table_data.json", "w", encoding="utf-8") as f:
                json.dump(self.elements, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("Export Successful", "Periodic table data exported to periodic_table_data.json")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Error exporting data: {str(e)}")

# Entry point of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableExplorer(root)
    root.mainloop()