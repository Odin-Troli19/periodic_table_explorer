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
        "electronegativity": 0.82,
        "density": 0.862,
        "melting_point": 336.53,
        "boiling_point": 1032,
        "discovered_by": "Humphry Davy",
        "year_discovered": 1807
    },
    "20": {
        "symbol": "Ca",
        "names": {
            "en": "Calcium",
            "pt": "Cálcio",
            "no": "Kalsium"
        },
        "atomic_number": 20,
        "atomic_mass": 40.078,
        "category": "alkaline earth metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s²",
        "electronegativity": 1.00,
        "density": 1.54,
        "melting_point": 1115,
        "boiling_point": 1757,
        "discovered_by": "Humphry Davy",
        "year_discovered": 1808
    },
    "21": {
        "symbol": "Sc",
        "names": {
            "en": "Scandium",
            "pt": "Escândio",
            "no": "Scandium"
        },
        "atomic_number": 21,
        "atomic_mass": 44.956,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹",
        "electronegativity": 1.36,
        "density": 2.985,
        "melting_point": 1814,
        "boiling_point": 3109,
        "discovered_by": "Lars Fredrik Nilson",
        "year_discovered": 1879
    },
    "22": {
        "symbol": "Ti",
        "names": {
            "en": "Titanium",
            "pt": "Titânio",
            "no": "Titan"
        },
        "atomic_number": 22,
        "atomic_mass": 47.867,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d²",
        "electronegativity": 1.54,
        "density": 4.507,
        "melting_point": 1941,
        "boiling_point": 3560,
        "discovered_by": "William Gregor",
        "year_discovered": 1791
    },
    "23": {
        "symbol": "V",
        "names": {
            "en": "Vanadium",
            "pt": "Vanádio",
            "no": "Vanadium"
        },
        "atomic_number": 23,
        "atomic_mass": 50.942,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d³",
        "electronegativity": 1.63,
        "density": 6.11,
        "melting_point": 2183,
        "boiling_point": 3680,
        "discovered_by": "Andrés Manuel del Río",
        "year_discovered": 1801
    },
    "24": {
        "symbol": "Cr",
        "names": {
            "en": "Chromium",
            "pt": "Crômio",
            "no": "Krom"
        },
        "atomic_number": 24,
        "atomic_mass": 51.996,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d⁵",
        "electronegativity": 1.66,
        "density": 7.15,
        "melting_point": 2180,
        "boiling_point": 2944,
        "discovered_by": "Louis Nicolas Vauquelin",
        "year_discovered": 1794
    },
    "25": {
        "symbol": "Mn",
        "names": {
            "en": "Manganese",
            "pt": "Manganês",
            "no": "Mangan"
        },
        "atomic_number": 25,
        "atomic_mass": 54.938,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁵",
        "electronegativity": 1.55,
        "density": 7.21,
        "melting_point": 1519,
        "boiling_point": 2334,
        "discovered_by": "Johann Gottlieb Gahn, Ignatius Gottfried Kaim",
        "year_discovered": 1774
    },
    "26": {
        "symbol": "Fe",
        "names": {
            "en": "Iron",
            "pt": "Ferro",
            "no": "Jern"
        },
        "atomic_number": 26,
        "atomic_mass": 55.845,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁶",
        "electronegativity": 1.83,
        "density": 7.874,
        "melting_point": 1811,
        "boiling_point": 3134,
        "discovered_by": "Ancient civilizations",
        "year_discovered": None
    },
    "27": {
        "symbol": "Co",
        "names": {
            "en": "Cobalt",
            "pt": "Cobalto",
            "no": "Kobolt"
        },
        "atomic_number": 27,
        "atomic_mass": 58.933,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁷",
        "electronegativity": 1.88,
        "density": 8.90,
        "melting_point": 1768,
        "boiling_point": 3200,
        "discovered_by": "Georg Brandt",
        "year_discovered": 1735
    },
    "28": {
        "symbol": "Ni",
        "names": {
            "en": "Nickel",
            "pt": "Níquel",
            "no": "Nikkel"
        },
        "atomic_number": 28,
        "atomic_mass": 58.693,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d⁸",
        "electronegativity": 1.91,
        "density": 8.908,
        "melting_point": 1728,
        "boiling_point": 3186,
        "discovered_by": "Axel Fredrik Cronstedt",
        "year_discovered": 1751
    },
    "29": {
        "symbol": "Cu",
        "names": {
            "en": "Copper",
            "pt": "Cobre",
            "no": "Kobber"
        },
        "atomic_number": 29,
        "atomic_mass": 63.546,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s¹ 3d¹⁰",
        "electronegativity": 1.90,
        "density": 8.96,
        "melting_point": 1357.77,
        "boiling_point": 2835,
        "discovered_by": "Ancient civilizations",
        "year_discovered": None
    },
    "30": {
        "symbol": "Zn",
        "names": {
            "en": "Zinc",
            "pt": "Zinco",
            "no": "Sink"
        },
        "atomic_number": 30,
        "atomic_mass": 65.38,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰",
        "electronegativity": 1.65,
        "density": 7.14,
        "melting_point": 692.68,
        "boiling_point": 1180,
        "discovered_by": "Indian metallurgists",
        "year_discovered": 1000
    },
    "31": {
        "symbol": "Ga",
        "names": {
            "en": "Gallium",
            "pt": "Gálio",
            "no": "Gallium"
        },
        "atomic_number": 31,
        "atomic_mass": 69.723,
        "category": "post-transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p¹",
        "electronegativity": 1.81,
        "density": 5.91,
        "melting_point": 302.91,
        "boiling_point": 2477,
        "discovered_by": "Lecoq de Boisbaudran",
        "year_discovered": 1875
    },
    "32": {
        "symbol": "Ge",
        "names": {
            "en": "Germanium",
            "pt": "Germânio",
            "no": "Germanium"
        },
        "atomic_number": 32,
        "atomic_mass": 72.630,
        "category": "metalloid",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p²",
        "electronegativity": 2.01,
        "density": 5.323,
        "melting_point": 1211.40,
        "boiling_point": 3106,
        "discovered_by": "Clemens Winkler",
        "year_discovered": 1886
    },
    "33": {
        "symbol": "As",
        "names": {
            "en": "Arsenic",
            "pt": "Arsênio",
            "no": "Arsen"
        },
        "atomic_number": 33,
        "atomic_mass": 74.922,
        "category": "metalloid",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p³",
        "electronegativity": 2.18,
        "density": 5.776,
        "melting_point": 1090,
        "boiling_point": 887,
        "discovered_by": "Ancient civilizations",
        "year_discovered": None
    },
    "34": {
        "symbol": "Se",
        "names": {
            "en": "Selenium",
            "pt": "Selênio",
            "no": "Selen"
        },
        "atomic_number": 34,
        "atomic_mass": 78.971,
        "category": "nonmetal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁴",
        "electronegativity": 2.55,
        "density": 4.809,
        "melting_point": 494,
        "boiling_point": 958,
        "discovered_by": "Jöns Jacob Berzelius",
        "year_discovered": 1817
    },
    "35": {
        "symbol": "Br",
        "names": {
            "en": "Bromine",
            "pt": "Bromo",
            "no": "Brom"
        },
        "atomic_number": 35,
        "atomic_mass": 79.904,
        "category": "halogen",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁵",
        "electronegativity": 2.96,
        "density": 3.1028,
        "melting_point": 265.8,
        "boiling_point": 332.0,
        "discovered_by": "Antoine Jérôme Balard, Carl Jacob Löwig",
        "year_discovered": 1826
    },
    "36": {
        "symbol": "Kr",
        "names": {
            "en": "Krypton",
            "pt": "Criptônio",
            "no": "Krypton"
        },
        "atomic_number": 36,
        "atomic_mass": 83.798,
        "category": "noble gas",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶",
        "electronegativity": 3.00,
        "density": 0.003733,
        "melting_point": 115.79,
        "boiling_point": 119.93,
        "discovered_by": "William Ramsay, Morris Travers",
        "year_discovered": 1898
    },
    "37": {
        "symbol": "Rb",
        "names": {
            "en": "Rubidium",
            "pt": "Rubídio",
            "no": "Rubidium"
        },
        "atomic_number": 37,
        "atomic_mass": 85.468,
        "category": "alkali metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s¹",
        "electronegativity": 0.82,
        "density": 1.532,
        "melting_point": 312.46,
        "boiling_point": 961,
        "discovered_by": "Robert Bunsen, Gustav Kirchhoff",
        "year_discovered": 1861
    },
    "38": {
        "symbol": "Sr",
        "names": {
            "en": "Strontium",
            "pt": "Estrôncio",
            "no": "Strontium"
        },
        "atomic_number": 38,
        "atomic_mass": 87.62,
        "category": "alkaline earth metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s²",
        "electronegativity": 0.95,
        "density": 2.64,
        "melting_point": 1050,
        "boiling_point": 1655,
        "discovered_by": "William Cruickshank",
        "year_discovered": 1790
    },
    "39": {
        "symbol": "Y",
        "names": {
            "en": "Yttrium",
            "pt": "Ítrio",
            "no": "Yttrium"
        },
        "atomic_number": 39,
        "atomic_mass": 88.906,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d¹",
        "electronegativity": 1.22,
        "density": 4.472,
        "melting_point": 1799,
        "boiling_point": 3609,
        "discovered_by": "Johan Gadolin",
        "year_discovered": 1794
    },
    "40": {
        "symbol": "Zr",
        "names": {
            "en": "Zirconium",
            "pt": "Zircônio",
            "no": "Zirkonium"
        },
        "atomic_number": 40,
        "atomic_mass": 91.224,
        "category": "transition metal",
        "electron_configuration": "1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰ 4p⁶ 5s² 4d²",
        "electronegativity": 1.33,
        "density": 6.52,
        "melting_point": 2128,
        "boiling_point": 4682,
        "discovered_by": "Martin Heinrich Klaproth",
        "year_discovered": 1789
    },