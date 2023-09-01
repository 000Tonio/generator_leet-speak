import itertools

def generate_leet_speak_combinations(word):
    leet_dict = {
        'a': ['a', '4', '@', 'A'],
        'b': ['b', '8', '6', 'B'],
        'c': ['c', '<', '¢', 'C'],
        'd': ['d', '|)', 'D'],
        'e': ['e', '3', '£', '€', 'ë', 'E'],
        'f': ['f', 'ph', 'F'],
        'g': ['g', '9', '6', '&', 'G'],
        'h': ['h', '#', 'H'],
        'i': ['i', '1', '|', '!', 'I'],
        'j': ['j', 'J'],
        'k': ['k', '|<', 'K'],
        'l': ['l', '1', '|', 'L'],
        'm': ['m', 'nn','M'],
        'n': ['n', 'N'],
        'o': ['o', '0', '°', '()', 'O'],
        'p': ['p', '9', 'q', 'P'],
        'q': ['q', '9', 'p', 'Q'],
        'r': ['r', '2', 'R'],
        's': ['s', '$', '5', 'z', '§', 'S'],
        't': ['t', '7', '+', '†', '|', '!', 'T'],
        'u': ['u', 'v', 'U'],
        'v': ['v', 'u', 'V'],
        'w': ['w', 'vv', 'W'],
        'x': ['x', '%', '><', 'X'],
        'y': ['y', 'j', 'Y'],
        'z': ['z', '2', 's', '5', 'Z'],
        '0': ['0', 'o', '°', '()', '[]', 'O'],
        '1': ['1', 'i', '|', '!'],
        '2': ['2', 'z', 's', '5', '7_'],
        '3': ['3', 'e', '£', '€', 'ë'],
        '4': ['4', 'a', '@'],
        '5': ['5', 's', '$', 'z', '§'],
        '6': ['6', 'g', '9'],
        '7': ['7', 't', '+', '†', '|'],
        '8': ['8', 'b', '|3', '|8'],
        '9': ['9', 'g', 'q'],
        '!': ['!', '1', '|', 'i'],
        '@': ['@', 'a', '4', 'A'],
        '#': ['#', 'h'],
        '$': ['$', 's', '5', 'z', '§'],
        '%': ['%', 'x', '><', '}{'],
        '^': ['^', 'v', 'u', 'w'],
        '&': ['&', 'g', '+'],
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
        ' ': [' '],  # Espace
        '\n': ['\n'],  # Retour à la ligne
        # Ajoutez d'autres correspondances de caractères spéciaux ou de chiffres au besoin
    }

    # Générer des chiffres de 00 à 99
    digits = [str(i).zfill(2) for i in range(10)]

    combinations = []
    for char_combinations in [leet_dict[char.lower()] for char in word]:
        combinations.append(char_combinations)

    # Produire toutes les combinaisons possibles des caractères spéciaux pour chaque lettre
    all_combinations = [''.join(combination) for combination in itertools.product(*combinations)]

    # Ajouter des chiffres de 00 à 99 à la fin de chaque combinaison
    final_combinations = [combination + digit for combination in all_combinations for digit in digits]

    return final_combinations

def process_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            words = text.split()

        converted_words = []
        for word in words:
            combinations = generate_leet_speak_combinations(word)
            converted_words.extend(combinations)

        with open(output_file, 'w') as file:
            file.write('\n'.join(converted_words))

        print(f"Toutes les combinaisons possibles ont été écrites dans '{output_file}'.")
    except FileNotFoundError:
        print(f"Le fichier '{input_file}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

def main():
    input_file = input("Entrez le nom du fichier d'entrée : ")
    output_file = input("Entrez le nom du fichier de sortie : ")

    process_text_file(input_file, output_file)

if __name__ == "__main__":
    main()
