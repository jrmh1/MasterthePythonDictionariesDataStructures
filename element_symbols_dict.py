element_symbols_dict = {
    'Hydrogen': 'H',
    'Helium': 'He',
    'Lithium': 'Li',
    'Beryllium': 'Be',
    'Boron': 'B',
    'Carbon': 'C',
    'Nitrogen': 'N',
    'Oxygen': 'O',
    'Fluorine': 'F',
    'Neon': 'Ne'
}


print("Entire dictionary:", element_symbols_dict)


sixth_element_symbol = list(element_symbols_dict.items())[5]
print("Symbol of the 6th element:", sixth_element_symbol)


element_symbols_dict['Oxygen'] = 'O2'


del element_symbols_dict['Fluorine']


last_element_symbol = list(element_symbols_dict.items())[-1]
print("Last key-value pair:", last_element_symbol)
