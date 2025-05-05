# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range

lista = list(range(0, 101, 4))

print(lista)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. 

lista = ["Hola", 3.14, True, 5, "TP 5"]

print(lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior

lista = []

lista.append("trabajo")
lista.append("practico")
lista.append("cinco")

print(lista)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"]
print(animales)

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]  # Crea la lista con numeros
numeros.remove(max(numeros)) # La funcion remove es para eliminar algun elemento de la lista, y max selecciona el valor mas alto
print(numeros)               # Imprime la lista luego de haber eliminado el valor mas alto de la lista

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros. 

nums = list(range(10, 31, 5))

print(nums[0:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"] 
print(autos)

autos [1:3] = ["vento", "passat"]
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla. 

numeros = [5, 10, 15]
dobles = []

for num in numeros:
         dobles.append(num * 2)

print(dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 

# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla 

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
print(compras)

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan") # Si quisiera usar indice: del compras[0][0]

print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

#               [0]  [1]    2[0]  2[1]  2[2]    [3]
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]


