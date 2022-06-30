
def encrypt(_message, _integer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    encryptedMsg = ""
    for i in range(len(_message)):
        if _message[i] in alphabet:
            encryptedMsg += alphabet[(alphabet.index(_message[i]) + _integer) % 26]
        elif _message[i] in ALPHABET:
            encryptedMsg += ALPHABET[(ALPHABET.index(_message[i]) + _integer) % 26]
        else:
            encryptedMsg += _message[i]
    return encryptedMsg

def decrypt(_message, _integer):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    decryptedMsg = ""
    for i in range(len(_message)):
        if _message[i] in alphabet:
            decryptedMsg += alphabet[(alphabet.index(_message[i]) - _integer) % 26]
        elif _message[i] in ALPHABET:
            decryptedMsg += ALPHABET[(ALPHABET.index(_message[i]) - _integer) % 26]
        else:
            decryptedMsg += _message[i]
    return decryptedMsg

if __name__ == "__main__":
    _integer = int(input())
    choice = int(input())
    _message = input()

    if choice == 0:
        print(encrypt(_message, _integer))
    elif choice == 1:
        print(decrypt(_message, _integer))
    else:
        print("Invalid choice")