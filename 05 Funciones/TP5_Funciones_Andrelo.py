#  1. Crear una función llamada imprimir_hola_mundo que imprima por
#  pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#  programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")
    
imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
#  como parámetro un nombre y devuelva un saludo personalizado.
#  Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
#  principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    print(f"Hola, {nombre} !")

saludar_usuario("Luciano")

#  3. Crear una función llamada informacion_personal(nombre, apellido,
#  edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#  [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
# dir los datos al usuario y llamar a esta función con los valores in
# gresados

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Pedir los datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

# LLamamos la función
informacion_personal(nombre, apellido, edad, residencia)

#  4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.
import math

# Definimos las funciones
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# Solicitamos el radio al usuario
radio = float(input("Ingrese el radio del circulo: "))

# Validamos que sea un numero positivo
while radio <= 0:
    radio = float(input("Error, ingrese un numero positivo: "))

# LLamamos las funciones y muestro resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El radio del circulo es {radio} y su area es {round(area, 2)}, y si perimetro es {round(perimetro, 2)}")


#  5. Crear una función llamada segundos_a_horas(segundos) que reciba
#  una cantidad de segundos como parámetro y devuelva la cantidad
#  de horas correspondientes. Solicitar al usuario los segundos y mos
# trar el resultado usando esta función.

# Armamos la funcion
def segundos_a_horas(segundos):
    horas = (segundos / 3600)
    return horas

# Solicitamos al usuario los segundos
segundos = int(input("Ingrese la cantidad de segundos para transformar a hora: "))

# Validamos que sea un numero positivo
while segundos < 0:
    segundos = int(input("Error, ingrese un numero positivo: "))

# LLamamos la funcion y mostramos el resultado
hora = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {hora} horas")

#  6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#  número como parámetro y imprima la tabla de multiplicar de ese
#  número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Creamos la funcion
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print (f"{i} x {numero} = {resultado}")

# Solicitar el numero al usuario
numero = int(input("Ingrese un numero del 1 al 10: "))

# Validamos que sea un numero positivo
while numero <= 0 or numero > 10:
    numero = int(input("Error, ingrese un numero del 1 al 10: "))

# LLamamos la funcion y mostramos el resultado
print(f"La tabla de multiplicar del numero {numero} es: ")
tabla_multiplicar(numero)

#  7. Crear una función llamada operaciones_basicas(a, b) que reciba
#  dos números como parámetros y devuelva una tupla con el resultado
#  de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
#  sultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b
    return (suma, resta, multi, div)

# Solicitamos al usuario los numeros
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

# Llamamos la funcion y guardamos el resultado en una variable
resultado = operaciones_basicas(a, b)
#print(resultado)

# Mostramos los resultados, ya que devuelve una tupla, accedemos a los valores mediante su index
print(f"""Suma: {resultado[0]}
Resta: {resultado[1]}
Multiplicación: {resultado[2]}
División: {resultado[3]}""")

#  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#  peso en kilogramos y la altura en metros, y devuelva el índice de
#  masa corporal (IMC). Solicitar al usuario los datos y llamar a la fun
# ción para mostrar el resultado con dos decimales.

# Creamos la funcion
def calcular_imc():
    peso = float(input("Indique su peso en kilogramos: ")) 
    altura =  int(input("Indique su altura en centimetros: ")) / 100
    # Validamos que sean numero positivos
    while peso <= 0 or altura <= 0:
        print("Error, ambos valores deben ser positivos")
        peso = float(input("Indique su peso en kilogramos: ")) 
        altura =  int(input("Indique su altura en centimetros: ")) / 100
    imc = peso / (altura ** 2)
    return imc

# Llamamos a la funcion
indice = calcular_imc()
print(f"Tu indice de masa corporal es: {round(indice, 2)}")

#  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#  una temperatura en grados Celsius y devuelva su equivalente en
#  Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#  resultado usando la función.

# Funcion
def celsius_a_farenheit(celsius):
    far = (celsius * 9/5) + 32
    return far

# Pedimos al usuario la temperatura
celsius = float(input("Indique la temperatura en Celsius: "))

# Llamamos la funcion y mostramos el resutlado
farenheit = celsius_a_farenheit(celsius)

print(f"{celsius}°C equivalen a {farenheit}°F")

#  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#  tres números como parámetros y devuelva el promedio de ellos.
#  Solicitar los números al usuario y mostrar el resultado usando esta
#  función.

# Funcion para calcular el promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Solicitamos al usuario los numeros
a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
c = float(input("Ingrese el tercer numero: "))

# Llamamos la funcion y mostramos el resultado
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio}")