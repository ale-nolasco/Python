# Hacer un programa que cuente del 1 al 100 que imprima solo los numeros pares

import os

os.system('cls')

print("\t\tPrograma que imprime numeros pares del 1 al 100")

for i in range(1,101):
    if i % 2:
        print(i+1)
input()

