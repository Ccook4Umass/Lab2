#!/usr/bin/env python
chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
data = open("CCcipher.txt", "r")
message = data.readline()
       
def decoder(message, shift=23):
    dec_chars = str.maketrans(
        f'{chars[0][shift:]}{chars[0][:shift]}{chars[1][shift:]}{chars[1][:shift]}',
        f'{chars[0]}{chars[1]}'
        )
    return str.translate(message, dec_chars)
    
    



    shift=23
    print(f'Decrypted Message: {decoder(message, shift)}')
chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
data = open("test.txt", "r")
message = data.readline()
       
def decoder(message, shift=23):
    dec_chars = str.maketrans(
        f'{chars[0][shift:]}{chars[0][:shift]}{chars[1][shift:]}{chars[1][:shift]}',
        f'{chars[0]}{chars[1]}'
        )
    return str.translate(message, dec_chars)
    
    


shift=23
print(f'Decrypted Message: {decoder(message, shift)}')
