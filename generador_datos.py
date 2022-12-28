import random

file_export = open('export.txt','w+')

cont = 0

while cont < 2000:
    numero = random.randint(1, 5000000)
    file_export.write(str(numero) + '\n')
    cont+=1

file_export.close()
                    