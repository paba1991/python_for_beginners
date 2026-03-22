# Solución esperada para el Reto: El Parque de Diversiones

# 1. Uso del bucle WHILE (Cuenta regresiva simple)
tiempo = 3

print("--- PREPARANDO EL PARQUE ---")
while tiempo > 0:
    print(f"Abriendo los juegos en {tiempo}...")
    tiempo -= 1  # Actualizamos la variable para no crear un bucle infinito

print("¡El parque está abierto! \n")

# 2. Uso del bucle FOR y CONDICIONALES (Procesamiento de lista)
estaturas = [140, 165, 120, 180, 110, 155]

print("--- REVISANDO ESTATURAS DE LA FILA ---")

for estatura in estaturas:
    # Evaluamos cada estatura con if / elif / else
    if estatura >= 150:
        print(f"Con {estatura}cm: Puedes subir a la Montaña Rusa Extrema ")
    elif estatura >= 120:
        print(f"Con {estatura}cm: Puedes subir a la Montaña Rusa Moderada ")
    else:
        print(f"Con {estatura}cm: Solo puedes subir a los Juegos Infantiles ")

print("\n¡Toda la fila ha sido revisada!")
