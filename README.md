# 🔐 Caesar Cipher

A simple command-line Caesar Cipher tool written in Python that lets you encrypt and decrypt messages using a classic substitution cipher.

## What is the Caesar Cipher?

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in a message by a fixed number of positions in the alphabet. For example, with a shift of 3:

```
A → D,  B → E,  C → F,  ...  Z → C
Hello → Khoor
```

Decryption simply reverses the shift.

## Features

- ✅ Encrypt any text message
- ✅ Decrypt previously encrypted messages
- ✅ Preserves spaces, punctuation, and numbers
- ✅ Handles both uppercase and lowercase letters
- ✅ Interactive command-line interface
- ✅ Input validation with helpful error messages

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository:

```bash
git clone https://github.com/mohityadav2410041-art/caesar-cipher.git
cd caesar-cipher
```

No external dependencies are required — it runs on the Python standard library.

### Usage

Run the script:

```bash
python app.py
```

You'll be prompted to choose a mode, enter your message, and provide a shift value:

```
Welcome to the Caesar Cipher Program!
Would you like to (encrypt) or (decrypt) a message? (Type 'exit' to quit): encrypt
Enter your message: Hello, World!
Enter the shift value (an integer): 3
Resulting message: Khoor, Zruog!
```

To decrypt the same message:

```
Would you like to (encrypt) or (decrypt) a message? (Type 'exit' to quit): decrypt
Enter your message: Khoor, Zruog!
Enter the shift value (an integer): 3
Resulting message: Hello, World!
```

Type `exit` to quit the program.

## How It Works

The core logic lives in the `caesar_cipher(text, shift, mode)` function:

- Each alphabetical character is shifted by the given amount using modular arithmetic (`% 26`), so the alphabet wraps around correctly.
- Non-alphabetical characters (spaces, punctuation, digits) are passed through unchanged.
- For decryption, the shift is simply negated.

## Project Structure

```
caesar-cipher/
└── app.py   # Main script with cipher logic and CLI
```

## Example

| Mode    | Input         | Shift | Output        |
|---------|---------------|-------|---------------|
| Encrypt | `Hello World` | 13    | `Uryyb Jbeyq` |
| Decrypt | `Uryyb Jbeyq` | 13    | `Hello World` |
| Encrypt | `Python 3.x`  | 5     | `Udymts 3.x`  |

> **Note:** A shift of 13 is a special case known as [ROT13](https://en.wikipedia.org/wiki/ROT13), where encrypting and decrypting use the same operation.

## Limitations

- The Caesar Cipher is not secure for real-world use — it can be broken easily with brute force (only 25 possible shifts).
- It is intended for educational purposes and fun.

## License

This project is open source and available under the [MIT License](LICENSE).
