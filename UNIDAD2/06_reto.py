cuenta = float(input(" Introduce el total de la Cuenta: $"))
propina_porcentaje = float(input("Introduce la Propina (%): "))
personas = int(input("Introduce el numero de Personas: "))

propina = cuenta * (propina_porcentaje / 100)
total = cuenta + propina
por_persona = total / personas

print(f"Total de la cuenta: ${total:.2f}")
print(f"Cada persona pagara: ${por_persona:.2f}")