##########################################
edad = 18
if edad > 18:
    print ("Eres mayor de edad")

##########################################
edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

##########################################
calificacion = 85
if calificacion >= 90:
  print("Calificación: A (Excelente)")
elif calificacion >= 80:
  print("Calificación: B (Bueno)")
elif calificacion >= 70:
  print("Calificación: C (Satisfactorio)")
else:
  print("Calificación: F (Reprobado)")

##########################################
frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
  print(f"Tengo una {fruta}")

##########################################
contador = 0
while contador < 5:
  print(f"Contador: {contador}")
  contador = contador + 1