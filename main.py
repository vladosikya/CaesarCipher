from art import logo
from alph import symbols
print(logo)

def encrypt():
    word = input("Enter a word or phrase to encrypt. ")
    encrypt_word = ""

    while True:
        shift = input("What shift? ")
        try:
            shift = int(shift)
            break
        except:
            pass

    for symb in word:
        if symb.lower() in symbols:
            if symb == symb.upper():
                up = True
            else:
                up = False
            symb = symb.lower()
            element_index = symbols.index(symb)
            new_element_index = element_index + shift

            while new_element_index > len(symbols)-1:
                new_element_index-=len(symbols)
            if up:
                encrypt_word+=(symbols[new_element_index]).upper()
            elif up == False:
                encrypt_word += (symbols[new_element_index])
        else:
            encrypt_word +=symb

    print(f"Result: {encrypt_word}")

def decrypt():
    word = input("Enter a word or phrase to decrypt. ")
    decrypt_word = ""

    while True:
        shift = input("What shift? ")
        try:
            shift = int(shift)
            break
        except:
            pass

    for symb in word:
        if symb.lower() in symbols:
            if symb == symb.upper():
                up = True
            else:
                up = False
            symb = symb.lower()
            element_index = symbols.index(symb)
            new_element_index = element_index - shift

            while abs(new_element_index) > len(symbols)-1:
                new_element_index += len(symbols)
            if up:
                decrypt_word += (symbols[new_element_index]).upper()
            elif up == False:
                decrypt_word += (symbols[new_element_index])
        else:
            decrypt_word += symb

    print(f"Result: {decrypt_word}")

while True:
    choose = input("Which operating mode do you want to choose? Write 'encrypt' to encrypt text or 'decrypt' to decrypt text. "
                   "Type 'exit' to exit the application. ").lower()
    if choose == "encrypt":
        encrypt()
    elif choose == "decrypt":
        decrypt()
    elif choose == "exit":
        break
    else:
        print("Unknown command. Try again.\n")