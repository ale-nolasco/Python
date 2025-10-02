# Hacer un programa que solicite un color por teclado e imprima “Puede pasar “ si el 
# color ingresado es verde , “Precaución “ si es amarillo , “No pasar “ si es rojo o “Color
# inválido” si es cualquier otro.
import os

resp = 1

while resp != 0: 

    os.system('cls')

    print("             Programa semaforo")

    color = input("\n\nIngrese un color(verde, amarillo, rojo): ")

    if color == "verde":
        print("Puede Pasar")
    elif color == "amarillo":
        print("Precaucion")
    elif color == "rojo":
        print("No Pasar")

    resp = int(input("Desea ingresar otro color (1=si,0 = no): "))
    if resp == 0:
        print("Adios")