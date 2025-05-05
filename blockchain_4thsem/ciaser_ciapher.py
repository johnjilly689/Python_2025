def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():
            if mode=="encrypt":
                shift_amount=shift
            else:
                shift_amount=-shift
            
            
            new_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
#   lets understood lat part:
# e.g        ord('z') - ord('a')  # 122 - 97 = 25 (Position of 'z')
# 25 + 3 = 28  # Shift forward
# 28 % 26 = 2  # Wrap around (Position 2 → 'c')
# chr(2 + ord('a')) = 'c'
            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result  # This must be inside the function

# Example usage
encrypted_text = caesar_cipher("Hello, Blockchain!", 3, "encrypt")
print("Encrypted:", encrypted_text)

# my written code
text=input("give a word: \n" )
def ciaser(text,shift_amount,mode="encrypt"):
    result=''
    for x in text:
        if x.isalpha():
            new_txt=chr(((ord(x.lower()))-ord("a")+shift_amount)%26 + ord("a"))
            result+=new_txt
        else:
            result+=x
    return result


encrypted_text=ciaser(text,3,mode="encrypt")
print("encryption text is", encrypted_text)