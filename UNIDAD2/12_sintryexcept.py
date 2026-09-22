while True:
    edad = int(input("Edad: "))

    if 0 <= edad <= 120:
         break
    print("La edad debe estar entre 0 y 120.")
    if type(edad) != int:
        print("Escribe un número entero.")

print(f"Edad registrada: {edad}")