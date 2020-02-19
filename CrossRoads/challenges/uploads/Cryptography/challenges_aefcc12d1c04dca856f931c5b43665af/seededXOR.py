import random

random.seed(10)

text = input("Enter text: ")
newtext = b""


for c in text:
    newtext += chr(ord(c) ^ int(random.random() * 128)).encode('utf-8')

print("Ciphered text: ", str(newtext))   
#CipherText=b"\nd:Y</('0[/\x1c ]^\x1fM"
