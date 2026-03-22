# Reto Práctico: El Parque de Diversiones

¡Hola, futuros desarrolladores! Para este reto, vamos a combinar todo lo aprendido creando el sistema de acceso de un parque de diversiones. 

**Objetivo:** Utilizar un bucle `while` para una cuenta regresiva, y luego un bucle `for` junto con condicionales para clasificar a los visitantes según su estatura.

**Instrucciones paso a paso:**

1. **La cuenta regresiva (Uso de `while`):**
   - Crea una variable llamada `tiempo` y asígnale el valor `3`.
   - Crea un bucle `while` que se repita mientras el tiempo sea mayor a 0.
   - Dentro del bucle, imprime: `"Abriendo los juegos en [tiempo]..."`
   - **¡No lo olvides!** Resta 1 a la variable tiempo en cada repetición para evitar un bucle infinito.
   - Al salir del bucle, imprime `"¡El parque está abierto! 🎪"`.

2. **Revisando la fila (Uso de `for` e `if / elif / else`):**
   - Copia la siguiente lista de estaturas (en centímetros) en tu código:
     `estaturas = [140, 165, 120, 180, 110, 155]`
   - Utiliza un bucle `for` para recorrer cada estatura de la lista.
   - Dentro del bucle, utiliza condicionales para imprimir a qué juego pueden subir:
     - Si la estatura es **mayor o igual a 150**, imprime: `"Con [estatura]cm: Puedes subir a la Montaña Rusa Extrema 🎢"`
     - Si la estatura está **entre 120 y 149**, imprime: `"Con [estatura]cm: Puedes subir a la Montaña Rusa Moderada 🎡"`
     - Si la estatura es **menor a 120**, imprime: `"Con [estatura]cm: Solo puedes subir a los Juegos Infantiles 🎠"`
