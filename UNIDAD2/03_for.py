# Trabajando con rangos con for
for numero in range(1, 4, 2):
    cuadrado = numero ** 2
    print(numero, cuadrado)


# Trabajando con listas con for y enumerate
materias = ["Python", "Linux", "Interfaces"]
for posicion, materia in enumerate(materias, start=1):
    print(f"{posicion}. {materia}")


# Trabajando con listas con for
materias = ["Python", "Linux", "Interfaces"]
for materia in materias:
    print(materia)


# Trabajando con cadenas con for
cadena = "0123456789ABCDEF"
for letra in cadena:
    print(letra)


# Accediendo a una posición de la cadena
print(cadena[15])


# Trabajando con índices con for
for i in range(0, 16):
    print(cadena[i])