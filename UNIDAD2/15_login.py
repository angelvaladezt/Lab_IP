MAX = 3
for intento in range(1, MAX + 1):
    usuario = input("Usuario: ").strip().lower()
    clave = input("Contraseña: ")

    if usuario == "alumno" and clave == "python123":
        print("Bienvenido")
        break

    print("Credenciales incorrectas")
else: 
    print("Acceso bloqueado")    

