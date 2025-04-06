# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
    print(i)

# # 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# # dígitos que contiene.
import math

# Pedimos al usuario un numero e inicializamos la variable digitos
num = int(input("Indica un numero: "))
digitos = 0

# Bucle para indicar la cantidad de digitos
if num == 0:
    digitos = 1
else: 
    while num != 0:
        num = math.trunc(num/10)
        digitos += 1

# Imprimimos la cantida dde digitos
print(f"La cantidad de digitos del numero es: {digitos}")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores. 

# Pedimos al usuario los numeros a sumar e inicializamos la variable acumuladora
num1 = int(input("Escribe dos numeros, primero el menor de ellos: "))
num2 = int(input("Escribe el segundo numero: "))
suma = 0

# Validamos que el primer numero sea menor que el segundo
while num1 == num2 or num2 < num1:
    print("Error, el primer numero debe ser menor al segundo")
    num1 = int(input("Indica el primer numero: "))
    num2 = int(input("Indica el segundo numero: "))

# Bucle para sumar los numeros
while num1 < num2-1:
    num1 += 1
    suma = suma + num1

print(f"La sumatoria de los numeros es: {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
# un 0. 

# Pedimos al usuario un numero e inicializamos la variable acumuladora
num = int(input("Ingrese un numero para iniciar la suma: "))
suma = 0

# Bucle para sumar los numeros indicados
while num != 0:
    suma = suma + num
    print(f"Hasta ahora la suma es: {suma}")
    num = int(input("Ingresa otro numero, o pulsa 0 para salir: "))

print(f"La suma de los numeros es: {suma}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 
import random

# Inicializamos el numero aleatorio, el numero y la variable acumuladora de intentos
num_random = random.randint(0, 9)
intentos = 0
num = 10

print("Bienvenido, solo podrás salir de este bucle una vez adivines el numero")

while num != num_random:
    num = int(input("Ingresa un numero del 0 al 9: "))
    if num < 0 or num > 9:
        print("Solo numeros del 0 al 9")
    else:
        intentos += 1

print(f"""Haz adivinado!
El numero era {num_random}
Necesitaste {intentos} intentos para salir""")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
# entre 0 y 100, en orden decreciente.

for num in range(100, 0, -1):
    if num % 2 == 0:
        print(num)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario. 

# Pedimos al usuario un numero que será el rango del bucle e inicializamos la variable acumuladora
num = int(input("Ingrese un numero positivo para calcular la suma: "))
suma = 0

# Validamos que el numero sea positivo
while num < 0:
    num = int(input("Error, el numero debe ser positivo, ingrese otro numero: "))

# Bucle para calcular la suma
for i in range(0, num+1):
    suma = suma + i

print(f"La suma de los numeros es: {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
# negativos y cuántos son positivos.

# Inicializamos variables
pares = 0
impares = 0
positivos = 0
negativos = 0
cant_num = 4  # Modificar a 100

# Bucle para contar pares, impares, positivos y negativos
for i in range(0, cant_num):
    num = int(input("Ingrese un numero: "))
    
    # Pares e impares
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    #Positivos y negativos
    if num > 0:
        positivos += 1
    else:
        negativos += 1

# Mostramos cuantos hay de cada uno
print(f"""Los numeros positivos son: {positivos}
Los numeros negativos son: {negativos}
Los numeros Pares son {pares}
Los numeros impares son: {impares}""")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
# media de esos valores

# Inicializamos valores
cant_num = 0 
suma = 0

# Bucle para sumar y calcular la media de los valores
while cant_num != 4: # Modificar a 100
    num = int(input("Ingrese un numero: "))
    suma = suma + num
    cant_num += 1

# Imprimimos resultado
print(f"""La suma de los valores es {suma}
Ingresó {cant_num} numeros, el promedio es: {suma / cant_num}""")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
import math

# Pedimos numero al usuario e inicializamos la variable del numero invertido
num = int(input("Ingrese un numero a invertir: "))
numInverso = 0

# Bucle para invertir los digitos
while num != 0:
    numInverso = (numInverso*10) + (num%10)
    num = math.trunc(num/10)

print(f"El numero ingresado a la inversa es: {numInverso}")