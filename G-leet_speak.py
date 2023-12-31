import itertools
import argparse
import os

def generate_all_leet_speak_combinations(word):
    leet_dict = {
        'a': ['a', '4', '@', 'á', 'à', 'â'],
        'b': ['b', '8', '6', '|3', '|8'],
        'c': ['c', '<', '{', '[', '(', '¢'],
        'd': ['d'],
        'e': ['e', '3', '£', '€', 'ë', 'é', 'è', 'ê'],
        'f': ['f', 'ph'],
        'g': ['g', '9', '6', '&', '(_+'],
        'h': ['h', '#'],
        'i': ['i', '1', '|', '!', 'í', 'î'],
        'j': ['j', '_|', '_/', '_]'],
        'k': ['k', '|<', '|{', ']['],
        'l': ['l', '1', '|', '7', '|_', '|.'],
        'm': ['m', 'nn'],
        'n': ['n', '^'],
        'o': ['o', '0', '°', '()', 'ö', 'ó', 'ô'],
        'p': ['p', '9', 'q', '|*', '|°'],
        'q': ['q', '9', 'p', '2'],
        'r': ['r', '2', '/2'],
        's': ['s', '$', '5', 'z', '§'],
        't': ['t', '7', '+', '†', '|', '!'],
        'u': ['u', 'v', 'ú', 'ü', 'û'],
        'v': ['v', 'u', '><'],
        'w': ['w', 'vv', 'uu'],
        'x': ['x', '%', '><', '}{'],
        'y': ['y', 'j', '`/'],
        'z': ['z', '2', 's', '5', '7_'],
        '0': ['0', 'o', '°', '()', '[]'],
        '1': ['1', 'i', '|', '!'],
        '2': ['2', 'z', 's', '5', '7_'],
        '3': ['3', 'e', '£', '€', 'ë'],
        '4': ['4', 'a', '@'],
        '5': ['5', 's', '$', 'z', '§'],
        '6': ['6', 'g', '9', '(_+', '()'],
        '7': ['7', 't', '+', '†', '|'],
        '8': ['8', 'b', '|3', '|8', ']['],
        '9': ['9', 'g', 'q', '(_+'],
        '!': ['!', '1', '|', 'i', ']['],
        '@': ['@', 'a', '4'],
        '#': ['#', 'h'],
        '$': ['$', 's', '5', 'z', '§'],
        '%': ['%', 'x', '><'],
        '^': ['^', 'v', 'u', 'w'],
        '&': ['&', 'g'],
        '*': ['*', 'p', '|°'],
        '(': ['(', 'c', '<', '{', '[', '¢'],
        ')': [')', 'o', '0', '°', '()'],
        '_': ['_', 'j', '_|', '|_', '|.'],
        '-': ['-', 'a', '4', '/'],
        '+': ['+', 't', '7', '†', '|'],
        '=': ['=', 'f', 'ph'],
        '/': ['/', 'k', '\\'],
        '\\': ['\\', 'k', '/'],
        '|': ['|', 'i', 'l', '1', '!'],
        '[': ['[', 'c', '<', '{', '(', '¢'],
        ']': [']', 'm', 'nn', '^^', ']['],
        '{': ['{', 'c', '<', '[', '('],
        '}': ['}', 'h', '|-|', '][-', '}{'],
        '<': ['<', 'c', '{', '[', '('],
        '>': ['>', 'v', 'u', 'w', '><'],
        ',': [','],
        '.': ['.', 'l', '|_', '|,'],
        ':': [':'],
        ';': [';'],
        '?': ['?'],
        '&': ['&'],
        ' ': [' '],  
        '\n': ['\n'],
        'à': ['à'],
        'â': ['â'],
        'á': ['á'], 
        'é': ['é'], 
        'è': ['è'],
    	'ê': ['ê'],
    	'ë': ['ë'],
    	'î': ['î'],
	    'ï': ['ï'],
	    'í': ['í'],
        'ô': ['ô'],
	    'ö': ['ö'],
	    'ó': ['ó'],
	    'û': ['û'],
	    'ü': ['ü'],
	    'ú': ['ú'],
	    'ç': ['ç'],
	    '¢': ['¢'],
    }

    # Générer des chiffres de 00 à 10
    digits = [str(i).zfill(2) for i in range(10)]

    combinations = []
    for char_combinations in [leet_dict[char.lower()] for char in word]:
        combinations.append(char_combinations)

    # Produire toutes les combinaisons possibles des caractères spéciaux pour chaque lettre
    all_combinations = [''.join(combination) for combination in itertools.product(*combinations)]

    # Ajouter des chiffres de 00 à 10 à la fin de chaque combinaison
    final_combinations = [combination + digit for combination in all_combinations for digit in digits]

    return final_combinations

def process_text_file(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
            words = text.split()

        converted_words = []
        for word in words:
            combinations = generate_all_leet_speak_combinations(word)
            converted_words.extend(combinations)

        output_file = f"{os.path.splitext(input_file)[0]}-leet-speak.txt"
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(converted_words))

        print(f"Toutes les combinaisons possibles ont été écrites dans '{output_file}'.")
    except FileNotFoundError:
        print(f"Le fichier '{input_file}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def main():
    parser = argparse.ArgumentParser(description="Générateur de 'Leet Speak' avec Combinaisons de Chiffres")
    parser.add_argument('input_file', help="Chemin du fichier d'entrée")

    args = parser.parse_args()
    input_file = args.input_file

    process_text_file(input_file)

if __name__ == "__main__":
    main()
