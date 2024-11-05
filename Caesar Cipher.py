#Caesar_Cipher
def caesar(text, shift, direction):
    result=""

    if direction== "decrypt": #adjusting shift for decryption
        shift= -shift

    for x in text:
        if x.isupper(): #for capital letters
            result+= chr((ord(x)+shift-65)%26+65)
        elif x.islower(): #for small letters
            result+= chr((ord(x)+shift-97)%26+97)
        else:
            resuilt+=x

    return result

#input for user
word=input("Enter your message: ")
shift=int(input("enter the shift value:"))
action= input("Enter 'encrypt' for encryption or 'decrypt' for decryption: ").lower()

if action=="encrypt":
    output=caesar(word,shift,"encrypt")
elif action=="decrypt":
    output=caesar(word, shift,"decrypt")
else:
    output="invalid action"

print(f"Result: {output}")