def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == "encrypt" else -shift
            new_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result  # This must be inside the function

# Example usage
encrypted_text = caesar_cipher("Hello, Blockchain!", 3, "encrypt")
print("Encrypted:", encrypted_text)