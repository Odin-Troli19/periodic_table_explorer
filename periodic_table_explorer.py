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
            "alkali metal": "#ff6666",
            "alkaline earth metal": "#ffdead",
            "transition metal": "#ffc0c0",
            "post-transition metal": "#cccccc",
            "metalloid": "#cccc99",
            "nonmetal": "#a0ffa0",
            "halogen": "#ffff99",
            "noble gas": "#c0ffff",
            "lanthanide": "#ffbfff",
            "actinide": "#ff99cc"
        }
        
        # Load element data
        self.elements = self.load_element_data()
        
        # Create GUI
        self.create_widgets()
    
    def load_element_data(self):
        # This is our element data with English, Portuguese, and Norwegian names
        elements_data = {
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
            },
            "3": {
                "symbol": "Li",
                "names": {
                    "en": "Lithium",
                    "pt": "Lítio",
                    "no": "Litium"
                },
                "atomic_number": 3,
                "atomic_mass": 6.94,
                "category": "alkali metal",
                "electron_configuration": "1s² 2s¹",
                "electronegativity": 0.98,
                "density": 0.534,
                "melting_point": 453.69,
                "boiling_point": 1615,
                "discovered_by": "Johan August Arfwedson",
                "year_discovered": 1817
            },
            "4": {
                "symbol": "Be",
                "names": {
                    "en": "Beryllium",
                    "pt": "Berílio",
                    "no": "Beryllium"
                },
                "atomic_number": 4,
                "atomic_mass": 9.0122,
                "category": "alkaline earth metal",
                "electron_configuration": "1s² 2s²",
                "electronegativity": 1.57,
                "density": 1.85,
                "melting_point": 1560,
                "boiling_point": 2742,
                "discovered_by": "Louis Nicolas Vauquelin",
                "year_discovered": 1798
            },
            "5": {
                "symbol": "B",
                "names": {
                    "en": "Boron",
                    "pt": "Boro",
                    "no": "Bor"
                },
                "atomic_number": 5,
                "atomic_mass": 10.81,
                "category": "metalloid",
                "electron_configuration": "1s² 2s² 2p¹",
                "electronegativity": 2.04,
                "density": 2.34,
                "melting_point": 2349,
                "boiling_point": 4200,
                "discovered_by": "Joseph Louis Gay-Lussac, Louis Jacques Thénard",
                "year_discovered": 1808
            },
            "6": {
                "symbol": "C",
                "names": {
                    "en": "Carbon",
                    "pt": "Carbono",
                    "no": "Karbon"
                },
                "atomic_number": 6,
                "atomic_mass": 12.011,
                "category": "nonmetal",
                "electron_configuration": "1s² 2s² 2p²",
                "electronegativity": 2.55,
                "density": 2.267,
                "melting_point": 3823,
                "boiling_point": 4300,
                "discovered_by": "Ancient civilizations",
                "year_discovered": None
            },
            "7": {
                "symbol": "N",
                "names": {
                    "en": "Nitrogen",
                    "pt": "Nitrogênio",
                    "no": "Nitrogen"
                },
                "atomic_number": 7,
                "atomic_mass": 14.007,
                "category": "nonmetal",
                "electron_configuration": "1s² 2s² 2p³",
                "electronegativity": 3.04,
                "density": 0.001251,
                "melting_point": 63.15,
                "boiling_point": 77.36,
                "discovered_by": "Daniel Rutherford",
                "year_discovered": 1772
            },
            "8": {
                "symbol": "O",
                "names": {
                    "en": "Oxygen",
                    "pt": "Oxigênio",
                    "no": "Oksygen"
                },
                "atomic_number": 8,
                "atomic_mass": 15.999,
                "category": "nonmetal",
                "electron_configuration": "1s² 2s² 2p⁴",
                "electronegativity": 3.44,
                "density": 0.001429,
                "melting_point": 54.36,
                "boiling_point": 90.20,
                "discovered_by": "Carl Wilhelm Scheele, Joseph Priestley",
                "year_discovered": 1774
            },
            "9": {
                "symbol": "F",
                "names": {
                    "en": "Fluorine",
                    "pt": "Flúor",
                    "no": "Fluor"
                },
                "atomic_number": 9,
                "atomic_mass": 18.998,
                "category": "halogen",
                "electron_configuration": "1s² 2s² 2p⁵",
                "electronegativity": 3.98,
                "density": 0.001696,
                "melting_point": 53.53,
                "boiling_point": 85.03,
                "discovered_by": "André-Marie Ampère, Humphry Davy",
                "year_discovered": 1810
            },
            "10": {
                "symbol": "Ne",
                "names": {
                    "en": "Neon",
                    "pt": "Neônio",
                    "no": "Neon"
                },
                "atomic_number": 10,
                "atomic_mass": 20.180,
                "category": "noble gas",
                "electron_configuration": "1s² 2s² 2p⁶",
                "electronegativity": None,
                "density": 0.0008999,
                "melting_point": 24.56,
                "boiling_point": 27.07,
                "discovered_by": "William Ramsay, Morris Travers",
                "year_discovered": 1898
            }
            # Add more elements here - In a real application, you'd include all 118 elements
            # You would continue the pattern for elements 11-118
        }
        
        return elements_data
    
    def create_widgets(self):
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
        try:
            with open("periodic_table_data.json", "w", encoding="utf-8") as f:
                json.dump(self.elements, f, ensure_ascii=False, indent=4)
            messagebox.showinfo("Export Successful", "Periodic table data exported to periodic_table_data.json")
        except Exception as e:
            messagebox.showerror("Export Failed", f"Error exporting data: {str(e)}")

# Add more elements function to extend the database
def add_more_elements():
    # This function would be used to add more elements to the database
    # In a real application, you would add all 118 elements
    pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableExplorer(root)
    root.mainloop()