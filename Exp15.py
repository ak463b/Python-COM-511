# Morse Code Dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '
}

# Function to convert text to Morse Code
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        morse_code += morse_code_dict[char] + ' '
    return morse_code

# Function to convert Morse Code to text
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in morse_code_dict.items():
            if code == value:
                text += key
    return text

# Main program
while True:
    print("Morse Code Translator")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        input_text = input("Enter the text to convert to Morse Code: ")
        morse_result = text_to_morse(input_text)
        print(f"Morse Code: {morse_result}")

    elif choice == '2':
        input_morse = input("Enter the Morse Code to convert to text: ")
        text_result = morse_to_text(input_morse)
        print(f"Text: {text_result}")

    elif choice == '3':
        print("Exiting the Morse Code Translator. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")