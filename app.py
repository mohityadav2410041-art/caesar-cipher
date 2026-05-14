def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift
        
    for char in text:
        if char.isalpha():
            
            ascii_offset = ord('A') if char.isupper() else ord('a')
            
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char
            
    return result

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        mode = input("Would you like to (encrypt) or (decrypt) a message? (Type 'exit' to quit): ").lower()
        if mode == 'exit':
            print("Goodbye!")
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid input. Please choose 'encrypt' or 'decrypt'.")
            continue
            
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value (an integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
            
        result = caesar_cipher(message, shift, mode)
        print(f"Resulting message: {result}\n")

if __name__ == "__main__":
    main()
