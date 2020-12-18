import string

mykey="ECE"
data = open("test.txt", "r")
input_text = data.readline()


ciphertext = []
matrix = []
encryption_tuple= []
row = 0
control = 0
source = string.ascii_uppercase



for row in range(len(source)):
    matrix.append([ x for i,x in enumerate(source) if i > row ])   
    for i,x in enumerate(source):
        if i <= row: matrix[row].append(x)

for x,y in enumerate(input_text.upper()):
    control = 0 if control % len(mykey) == 0 else control
    if y in string.punctuation or y in string.whitespace:
         encryption_tuple.append((y,y))
    else:
         encryption_tuple.append((y,mykey[control]))
         control += 1

for x,y in encryption_tuple:
    if source.find(x) == -1: 
        ciphertext.append(x)
    else:
        ref_row = matrix[0].index(y)
        ciphertext.append(matrix[ref_row][source.index(x)])


print("-> Encrypted Messaged {0}".format(''.join(ciphertext)))
