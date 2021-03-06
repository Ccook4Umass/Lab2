#!/usr/bin/env python
chars = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz']
data = open("test.txt", "r")
message = data.readline()
def encoder(message, shift=23):
    enc_chars = str.maketrans(
        f'{chars[0]}{chars[1]}',
        f'{chars[0][shift:]}{chars[0][:shift]}{chars[1][shift:]}{chars[1][:shift]}' 
        )
    return str.translate(message, enc_chars)
        

shift=23
print(f'Encrypted Message: {encoder(message, shift)}')
