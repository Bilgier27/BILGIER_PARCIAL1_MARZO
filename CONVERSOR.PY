temperatura = 0
opcion = None
while opcion != 'finalizar':
    print("<<<< MENU DE OPCIONES >>>>\n\n1. Convertir de Celsius a Fahrenheit ->\n2. Convertir de Fahrenheit a Celsius ->\n3. Finalizar ->\n ->")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
        print(f"{temperatura} grados Celsius es igual a {(temperatura * 9/5) + 32} grados Fahrenheit")
    elif opcion == '2':
        temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        print(f"{temperatura} grados Fahrenheit es igual a {(temperatura - 32) * 5/9} grados Celsius")
    elif opcion == '3':
        print("Finalizar")
        opcion = 'finalizar' 
    else:
        print("Opción inválida, intente de nuevo")
