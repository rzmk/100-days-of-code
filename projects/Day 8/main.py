import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    final_text = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            if direction == "encode":
                letter_index += shift
                if letter_index >= 26:
                    letter_index -= 26
            elif direction == "decode":
                letter_index -= shift
            final_text += alphabet[letter_index]
        else:
            final_text += letter
    print(f"Here's the result: {final_text}")

def cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        cipher()
    else:
        return

print(art.logo)
cipher()