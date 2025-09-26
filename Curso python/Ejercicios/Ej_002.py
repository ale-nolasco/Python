# Hacer un programa que solicite por teclado dos numero y muestre la suma , la resta ,la 
# multiplicacion y la division de esos numero

print("             Programa de operaciones basicas")

a = int(input("\n\nIngrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
suma = a+b
resta = a-b
multi = a*b
div = a/b
# Suma

print(f"La suma de {a} + {b} = {suma}") 

# Resta

print(f"La resta de {a} - {b} = {resta}") 

# Multiplicacion 

print(f"La multiplicacion de {a} * {b} = {multi}") 

# Division

print(f"La division de {a} / {b} = {div}")