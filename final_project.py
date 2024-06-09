# This program encrypts and decrypts the message
from art import logo

is_program_continue = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
len_alphabet = len(alphabet)

print(logo)


def caesar(mode, message, shift_amount):
    final_text = ""

    if mode == "decode":
        shift_amount *= -1

    for char in message:
        if char in alphabet:
            index = alphabet.index(char)

            new_index = (index + shift_amount) % len_alphabet
            final_text += alphabet[new_index]

        else:
            final_text += char
    print(f"{direction}d message is: {final_text}")


while is_program_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(mode=direction, message=text, shift_amount=shift)
    is_program_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
