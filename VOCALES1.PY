#Crear programa que solicite al usuario una vocal
contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
vocales = 0

while True:
    entrada = input("Ingresa una vocal (o '1' para salir): ")

    if entrada == "1":
        break

    if entrada in contador_vocales:
        contador_vocales[entrada] += 1
        vocales += 1

print("\nvocales contadas:")
print(f'La cantidad de vocales ingresadas es: {contador_vocales}')

