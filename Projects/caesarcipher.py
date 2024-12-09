import pyfiglet

# importing pyfiglet for ascii art 

# printing ascii art for program name

START_ART = pyfiglet.figlet_format("CAESAR CIPHER") 
print(START_ART)

# creating cypher function 

# encodes or decodes a text using a caesar cipher

# caesar ciphers can be easily decoded by ANYONE!

def caesar_cipher(text, shift, mode='encode'):
    result = []
    if mode == 'decode':
        shift = -shift                       # reverse of shift for decoding purposes
        
    for char in text:
        if char.isalpha():                   
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)               # non-alphabetic characters remain unchanged
    
    return ''.join(result)

# user input

while True:
    print("/nWelcome to Caesar's Cipher!")
    mode = input("Type 'encode to encrypt, 'decode' to decrypt, or 'exit' to quit: ").lower()
    if mode == 'exit':
        print("Goodbye!")
        break
    if mode not in ['encode', 'decode']:
        print("Invalid input. Please choose 'encode' or 'decode'.")
        continue
    
    text = input("Enter your message: ")
    shift = int(input("Enter the shift number:"))

    # applying cipher

    transformed_text = caesar_cipher(text, shift, mode)
    print(f"The {mode}d text is: {transformed_text}")
