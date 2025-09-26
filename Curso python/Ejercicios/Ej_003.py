# Hacer un programa que solicite una edad y determine si es mayor de edad

edad = 0
while edad <= 0:
    
    print("     Programa que solicite edad y determine si es mayor de edad")

    edad = int(input("\n\nIngrese su edad: "))

    if edad < 0:
        print("La edad ingresada no es valida, ingrese edad nuevamente")  
    elif edad >= 18:

        print("Es Mayor de edad")
