import string

mykey="ECE"
data = open("VCcipher.txt", "r")
encoded = data.readline()


source = string.ascii_uppercase
shift = 23
matrix = [ source[(i + shift) % 26] for i in range(len(source)) ]
def decoder(thistext):
    control = 0
    plaintext = []

    for x,i in enumerate(encoded.upper()):
        if i not in source: 
            
            plaintext.append(i)
            continue
        else:
           
            control = 0 if control % len(mykey) == 0 else control 
            result = (matrix.index(i) - matrix.index(mykey[control])) % 26
            plaintext.append(source[result])
            control += 1
    return plaintext
print("-> Decoded text: {0}".format(''.join(decoder(encoded)).lower()))
