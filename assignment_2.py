def shift_letters(letter, n, encrypt=True):
    n_ = n % 26 
    result = " "
    if ord(letter) == 32: 
        result += ''
    else:
        if encrypt:
            result = chr(ord(letter) + n_)
        else:
            result = chr(ord(letter) - n_)

    if 'a' <= letter <= 'z':
        if encrypt:
            result = chr(((ord(letter) - ord('a') + n_) % 26) + ord('a'))
        else:
            result = chr(((ord(letter) - ord('a') - n_) % 26) + ord('a'))
        
    elif 'A' <= letter <= 'Z':
        if encrypt:
            result = chr(((ord(letter) - ord('A') + n_) % 26) + ord('A'))
        else:
            result = chr(((ord(letter) - ord('A') - n_) % 26) + ord('A'))

    return result

def Caesar_cipher(text, shift, encrypt=True):
    result = ""
    for letter in text:
        result += shift_letters(letter, shift, encrypt)
    return result
        


print("WELCOME TO CAESAR CIPHER!\n")
while True:
    print("Would you like to cipher or decipher a text? Choose 1 for Cipher, 2 for Decipher, or 3 to exit.")
    select = input()

    if select == '1':
        print("What is the message you want to cipher and by how many characters would you want to shift?")
        message = input("Message: ")
        key = input("Key: ")
        print(Caesar_cipher(message, int(key)))
    elif select == '2':
        print("What is the message you want to decipher and by how many characters would you want to shift?")
        message = input("Message: ")
        key = input("Key: ")
        print(Caesar_cipher(message, int(key), encrypt=False))
    elif select == '3':
        break
    else:
        print("Please select correct input")
    
