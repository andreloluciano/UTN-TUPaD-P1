#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

message = "Hola Mundo!"

print(message)

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
# realizar la impresión por pantalla. 

nombre = input("Ingrese un nombre: ")

print(f"Hola, {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
# años y vivo en Argentina”

# se piden datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
lugar = input("Dónde vives?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

# entrada de datos
radio = float(input("Indique el radio del circulo para calcular su area y perimetro: "))

# calculo de area
area = 3.14 * (radio**2)

# calculo del perimetro
perimetro = (2 * 3.14 * radio)

print(f"El area del circulo es {area}, y su perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
# cuántas horas equivale. 

# se pide al usuario que escriba los segundos
segundos = int(input("Indique la cantidad de segundos que desea calcular: "))

# calculo de segundos a hora
horas = segundos / 3600

print(f"Los {segundos} segundos equivalen a {round(horas, 2)} horas")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número. 
 
# pedimos al usuario un numero
num = int(input("Indique el numero del que desea ver la tabla: "))

# hay tabla
print(f"{num} x 1 = {num * 1}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

# se pide entrada de numeros
num1 = int(input("Ingrese un numero mayor a 0: "))
num2 = int(input("Ingrese otro numero mayor a 0: "))

# cuentas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

# resultados
print(f"La suma de los numeros es: {suma}")
print(f"La resta de los numeros es: {resta}")
print(f"La multiplicacion de los numeros es: {multiplicacion}")
print(f"La division de los numeros es: {division}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal.

# entrada de peso y altura
peso = int(input("Indique su peso en kilogramos: "))
alto = float(input("Indique si altura en centimetros: "))

# pasamos cm a m2
altura = (alto / 100)**2

# calculo indice de masa
masa = peso / altura

print(f"su indice de masa corporal es de {round(masa, 2)}")

#  9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
# pantalla su equivalente en grados Fahrenheit

# entrada de temperatura
temp = int(input("Indique un temeratura en Celsius: "))

# # Celsius a Farenheit
faren = (temp * 1.8) + 32

print (f"La temperatura {temp}°C son {faren}°F en Farenheit")

#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 

# se pide al usuario las tres notas
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))

# se calcula el promedio
promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio de las notas es: {promedio}")


