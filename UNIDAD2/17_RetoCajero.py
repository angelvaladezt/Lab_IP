def login():
    Usuario = "alumno"
    Clave = "python123"
    usuario= input("Usuario: ").strip().lower()
    clave= input("Clave: ").strip()
    if usuario == Usuario and clave == Clave:
       main()
    else:
        print("Credenciales incorrectas")
        
def consultar_saldo():
    print("Saldo: $0.00")
def depositar ():
    print("Depósito seleccionado")
def retirar():
    print("Retiro seleccionado")
def salir():
    print("Saliendo del cajero automatico...")

def mostrar_menu():
    print("Bienvenido al cajero automatico")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")
    return input("Opcion: ").strip()

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar()
        elif opcion == "3":
            retirar()
        elif opcion == "4":
            salir()
            break
        else:
            print("Opción inválida")
login()