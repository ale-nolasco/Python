# Hacer un programa que cuente del 1 al 100 inclusive e imprima 
# los numeros que son divisibles por 2 y por 5

import os

os.system('cls')
print("""\t\tPrograma que imprime numeros del 1 al 100 
      \t\t     divisibles por 2 y por 5 """)

for i in range(101):
    if (i % 2 == 0) and (i % 5 == 0):
        print(i)
