# This file contains a more comprehensive list of elements that you can add to the main program
# Just replace the elements dictionary in the load_element_data() function with this more complete one

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
    },
    "11": {
        "symbol": "Na",
        "names": {
            "en": "Sodium",
            "pt": "Sódio",
            "no": "Natrium"
        },
        "atomic_number": 11,
        "atomic_mass": 22.990,
        "category": "alkali metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s¹",
        "electronegativity": 0.93,
        "density": 0.971,
        "melting_point": 370.87,
        "boiling_point": 1156,
        "discovered_by": "Humphry Davy",
        "year_discovered": 1807
    },
    "12": {
        "symbol": "Mg",
        "names": {
            "en": "Magnesium",
            "pt": "Magnésio",
            "no": "Magnesium"
        },
        "atomic_number": 12,
        "atomic_mass": 24.305,
        "category": "alkaline earth metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s²",
        "electronegativity": 1.31,
        "density": 1.738,
        "melting_point": 923,
        "boiling_point": 1363,
        "discovered_by": "Joseph Black",
        "year_discovered": 1755
    },
    "13": {
        "symbol": "Al",
        "names": {
            "en": "Aluminum",
            "pt": "Alumínio",
            "no": "Aluminium"
        },
        "atomic_number": 13,
        "atomic_mass": 26.982,
        "category": "post-transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p¹",
        "electronegativity": 1.61,
        "density": 2.70,
        "melting_point": 933.47,
        "boiling_point": 2792,
        "discovered_by": "Hans Christian Ørsted",
        "year_discovered": 1825
    },
    "14": {
        "symbol": "Si",
        "names": {
            "en": "Silicon",
            "pt": "Silício",
            "no": "Silisium"
        },
        "atomic_number": 14,
        "atomic_mass": 28.085,
        "category": "metalloid",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p²",
        "electronegativity": 1.90,
        "density": 2.3290,
        "melting_point": 1687,
        "boiling_point": 3538,
        "discovered_by": "Jöns Jacob Berzelius",
        "year_discovered": 1824
    },
    "15": {
        "symbol": "P",
        "names": {
            "en": "Phosphorus",
            "pt": "Fósforo",
            "no": "Fosfor"
        },
        "atomic_number": 15,
        "atomic_mass": 30.974,
        "category": "nonmetal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p³",
        "electronegativity": 2.19,
        "density": 1.82,
        "melting_point": 317.30,
        "boiling_point": 553.65,
        "discovered_by": "Hennig Brand",
        "year_discovered": 1669
    },
    "16": {
        "symbol": "S",
        "names": {
            "en": "Sulfur",
            "pt": "Enxofre",
            "no": "Svovel"
        },
        "atomic_number": 16,
        "atomic_mass": 32.06,
        "category": "nonmetal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁴",
        "electronegativity": 2.58,
        "density": 1.96,
        "melting_point": 388.36,
        "boiling_point": 717.87,
        "discovered_by": "Ancient civilizations",
        "year_discovered": None
    },
    "17": {
        "symbol": "Cl",
        "names": {
            "en": "Chlorine",
            "pt": "Cloro",
            "no": "Klor"
        },
        "atomic_number": 17,
        "atomic_mass": 35.45,
        "category": "halogen",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁵",
        "electronegativity": 3.16,
        "density": 0.003214,
        "melting_point": 171.65,
        "boiling_point": 239.11,
        "discovered_by": "Carl Wilhelm Scheele",
        "year_discovered": 1774
    },
    "18": {
        "symbol": "Ar",
        "names": {
            "en": "Argon",
            "pt": "Argônio",
            "no": "Argon"
        },
        "atomic_number": 18,
        "atomic_mass": 39.948,
        "category": "noble gas",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶",
        "electronegativity": None,
        "density": 0.0017837,
        "melting_point": 83.80,
        "boiling_point": 87.30,
        "discovered_by": "Lord Rayleigh, Sir William Ramsay",
        "year_discovered": 1894
    },
    "19": {
        "symbol": "K",
        "names": {
            "en": "Potassium",
            "pt": "Potássio",
            "no": "Kalium"
        },
        "atomic_number": 19,
        "atomic_mass": 39.098,
        "category": "alkali metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹",