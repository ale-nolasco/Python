# Hacer un programa que imprima una tabla de multiplicar del 2 al 9 .
# Cada uno debe mostrar sus valores multiplicados del 1 al 9 inclusive

import os

os.system('cls')

print("\t\tTablas de multiplicar")

for i in range(2,10):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("\n")

input()
print("Adios :)")