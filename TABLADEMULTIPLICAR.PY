numero = int(input("Introduzca un número entero positivo: "))

if numero > 0:
    print(f"\nTabla de multiplicar del {numero}:\n")
    contador = 1
    while contador < 10:
        print(f"{numero} x {contador} = {numero * contador}")
        contador += 1
else:
    print("El número introducido no es positivo.")
