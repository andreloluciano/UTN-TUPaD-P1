# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 

# Solicitamos edad
edad = int(input("Escriba su edad: "))

# Condicional
if edad >= 18:
    print("Es mayor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
# mensaje “Desaprobado”. 

# Solicitamos la nota
nota = int(input("Ingrese la nota del alumno: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
# contrario, imprimir por pantalla "Por favor, ingrese un número par".

#Solicitamos al usario un numero
num = int(input("ingrese un numero: "))

# Condocional
if num % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
# siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# Defino variables para representar lo limites
limite_nino = 12
limite_adolescente = 18
limite_adulto_joven = 30

# Solicito edad al usuario
edad = int(input("Ingrese su edad: "))

# Condicional para darle categoria
if edad < limite_nino:
    print("Categoria Niño/a")
elif edad <= limite_adolescente:
    print("Categoria Adolescente")
elif edad <= limite_adulto_joven:
    print("Categoria Adulto/a")
else:
    print("Categoria Adulto Mayor")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

# Pedimos al usuario una contraseña
password = input("Ingrese su contraseña: ")

# Condicional para verificar la longitud de la contraseña
if len(password) < 8 or len(password) > 14:
    print("Error, ingrese una contraseña entre 8 y 14 caracteres")
else:
    print("Ha ingresado una contraseña correcta")

# 6)  escribir un programa que tome la lista 
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
print(numeros_aleatorios)

# Calculo de media, mode y mean
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Condicional para ver determinar el sesgo
if media > mediana > moda:
    print("Hay sesgo positivo, hacia la derecha")
elif media < mediana < moda:
    print("Hay sesgo negativo, hacia la izquierda")
else:
    print("No hay sesgo")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
# pantalla. 
# https://youtu.be/k9TUPpGqYTo?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&t=312

# Solicitamos frase al usuario
mensaje = input("Escriba una frase: ").lower()

# Verificamos si la ultima letra es vocal
if mensaje[-1] not in ("a", "e", "i", "o", "u"):    
    print(mensaje)
else:
    print(mensaje, "!")

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Solicitamos al usuario un nombre
nombre = input("Escriba su nombre: ")

# Solicitamos que indique un numero
num = int(input(""" Indique un numero:"
1 para mayusculas
2 para minusculas
3 para camelcase: """))

if num == 1:
    print(nombre.lower())
elif num == 2:
    print (nombre.upper())
elif num == 3:
    print(nombre.capitalize())
else:
    print("Error, debe ingresar 1, 2 o 3")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
# por pantalla: 
# ● Menor que 3: "Muy leve" (imperceptible). 
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
# ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
# generalmente no causa daños). 
# ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
# débiles). 
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

# # Defino variables para representar los limites
muy_leve = 3
leve = 4
moderado = 5
fuerte = 6
muy_fuerte = 7

# # Solicito al usuario la magnitud
escala = float(input("Indique la magnitud del terremoto segun la escala de Richter"))

# Condicional para evaluar su categoria
if escala < muy_leve:
    print("Muy leve, imperceptible")
elif escala < leve:
    print("Leve, ligeramente perceptible")
elif escala < moderado:
    print("Moderado, sentido por personas, pero no causa daños")
elif escala < fuerte:
    print("Fuerte, puede causar daños en estructuras debiles")
elif escala < muy_fuerte:
    (print("Muy Fuerte, puede causar daños significativos"))
else:
    print("Extremo, puede causar daños a gran escala")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicitamos la información al usuario
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1 para enero, 2 para febrero, etc.): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinar la estación según el hemisferio y la fecha
# Hemisferio Norte
if hemisferio == "N":  
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"

# Hemisferio Sur
elif hemisferio == "S":  
    if (mes == 12 and dia >= 21) or (mes == 1 or mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4 or mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7 or mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes == 10 or mes == 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"

# Mostrar la estación
print(f"La estación es: {estacion}")
