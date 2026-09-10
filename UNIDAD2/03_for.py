for numero in range(1, 7): # Trabajando con rangos con for
    cuadrado = numero ** 2
    print(numero, cuadrado)

materias = ["Python", "Linux", "Interfaces"]  #Trabajando listas con for y enumerate

for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}. {materia}")

for materia in materias:
    print(materia)

cadena = "0123456789ABCDEF"
for letra in cadena:
    print(letra)

for i in range (len(cadena)):
    print(cadena[i])

for numero in range (0,7,3):
    cuadrado = numero**2
    print(numero,cuadrado)