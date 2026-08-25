alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode" or encode_or_decode == "decode":
        if encode_or_decode == "decode":
            shift_amount *= -1

        output_value = ""
        for f in original_text:
            if f == " ":
                output_value += f
            else:
                temp = (alphabet.index(f) + shift_amount) % len(alphabet)
                output_value += alphabet[temp]
        print(f"Here is the {encode_or_decode}d result: {output_value}")

    else:
        print(f"'{encode_or_decode}': is not a Caesar cipher option")

caesar(text, shift, direction)