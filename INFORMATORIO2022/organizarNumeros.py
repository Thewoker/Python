numeros[3] = [None]
altNumero[3] = [None]

for x in range(0, 3):
    variable = input(f"Ingresa un numero en la posicion {x}")
    numeros[x]= int(variable)


for y in range(0, 3):
    if numeros[y] > numero[(y+1)]:
        altNumero[y] = numero[(y+1)]
        altNumero[(y+1)] = numero[y]

    print(altNumero[y]) 

