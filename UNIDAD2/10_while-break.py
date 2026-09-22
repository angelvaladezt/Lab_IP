while True:
    opcion = input("Elige A, B o C: ").strip().upper()

    if opcion in ("A", "B", "C"):
        break

    print("Opción inválida. Intenta de nuevo.")

print(f"Elegiste {opcion}")