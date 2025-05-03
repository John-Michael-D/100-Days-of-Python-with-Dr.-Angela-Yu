import sys

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   

           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

while True:

    directionInput = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().strip()
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))


    def caesar(direction):
        """This is the main function containing the encrypt and decrypt functions."""

        if direction == "encode":

            def encrypt(originalText, shiftAmount):
                """This function creates the ciphertext based on the cleartext (originalText)."""
                cleartext = ""
                ciphertext = ""

                for i in originalText:
                    cleartext += i

                for i in cleartext:
                    for index, value in enumerate(alphabet):
                        if i == value:
                            currentPosition = index
                            shiftedLetter = alphabet[(currentPosition + shiftAmount) % len(alphabet)]
                            ciphertext += shiftedLetter
                    if i not in alphabet and i != " ":
                        ciphertext += i

                print(f"Here is your ENCRYPTED message: {ciphertext}")

            encrypt(text, shift)

        if direction == "decode":

            def decrypt(cipherText, shiftAmount):
                """This function decrypts the ciphertext based on the given shiftAmount."""
                encryptedText = ""
                cleartext = ""

                for i in cipherText:
                    encryptedText += i

                for i in encryptedText:
                    for index, value in enumerate(alphabet):
                        if i == value:
                            currentPosition = index
                            shiftedLetter = alphabet[(currentPosition - shiftAmount) % len(alphabet)]
                            cleartext += shiftedLetter
                    if i not in alphabet and i != " ":
                        cleartext += i

                print(f"Here is your DECRYPTED message: {cleartext}")

            decrypt(text, shift)


    caesar(directionInput)

    while True:
        restart = input(
            "\nWould you like to encode or decode another message? Enter Y for yes or N for no:\n").lower().strip()

        try:
            if restart == "y":
                break
            elif restart == "n":
                print("Have a good one!")
                sys.exit()
            else:
                print("Invalid entry! Enter only 'y' or 'n'!")
        except ValueError:
            print("Try again!")
