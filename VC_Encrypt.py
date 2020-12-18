import string

mykey="ECE"
data = open("test.txt", "r")
input_mes = data.readline()

source = string.ascii_uppercase
shift = 23
matrix = [ source[(i + shift) % 26] for i in range(len(source)) ]
def coder(thistext):
    ciphertext = []
    control = 0

    for x,i in enumerate(input_mes.upper()):
        if i not in source: 
            ciphertext.append(i)
            continue
        else:
            control = 0 if control % len(mykey) == 0 else control 
            result = (source.find(i) + matrix.index(mykey[control])) % 26
            ciphertext.append(matrix[result])
            control += 1

    return ciphertext
print("-> Coded text: {0}".format(''.join(coder(input_mes)).lower()))
