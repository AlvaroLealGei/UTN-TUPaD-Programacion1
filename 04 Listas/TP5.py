"""
EJERCICIO 1

notas = [7.6, 8.5, 9.0, 6.5, 7.0, 8.0, 9.5, 7.8, 6.0, 8.2]
n=len(notas)
contador=0
suma=0

for nota in (notas):
    suma+=nota
    print(f"Nota {contador+1}: {nota}")
    contador+=1
notas.sort()
promedio=suma/n
print(f"Promedio: {promedio}")
print(f"La nota mas baja es: {notas[0]}, mientras que la nota mas alta es: {notas[n-1]}")

-----------------------------------------------
EJERCICIO 2
productos = []
    
for i in range(5):
    producto=input(f"Ingrese el nombre del producto n°{i+1}: ").lower()
    while producto.strip() == "":     
        print("No se pueden ingresar productos vacíos, por favor ingrese un producto válido.")
        producto=input(f"Ingrese el nombre del producto n°{i+1}: ").lower()
    productos.append(producto)
print("Los productos ingresados son:")
for producto in productos: 
    print(producto)
productos.sort()
print("Los productos ordenados alfabéticamente son:")
for producto in productos: 
    print(producto)
productoEliminado=input("Ingresa el producto de la lista que deseas eliminar: ").lower()
   
if productoEliminado in productos:
    productos.remove(productoEliminado)
else:
    print("El producto no se encuentra en la lista")
print("La lista de productos actualizada es:")
for producto in productos: 
    print(producto)
------------------------------------------------
EJERCICIO 3

import random
numeros = [random.randint(1,100) for i in range(15)]
numerosP = []
numerosI = []
print("Los números generados son:")
for i in range(len(numeros)):
    numero=numeros[i]
    print(f"{i+1}: {numero}")
    if numero%2==0:
        numerosP.append(numero)
    else:
        numerosI.append(numero)
print(f"Los numeros pares son: {numerosP} y los numeros impares son: {numerosI}")
print(f"La lista de los pares tienen {len(numerosP)} elementos, mientras que la lista de los impares tienen {len(numerosI)} elementos")

------------------------------------------------
EJERCICIO 4
datos = [1,3,5,3,7,1,9,5,3]
datosSinRepetidos = []
for dato in datos:
    if dato not in datosSinRepetidos:
        datosSinRepetidos.append(dato)
print(f"Los datos sin repetidos son: {datosSinRepetidos}")

------------------------------------------------
EJERCICIO 5
nombres = ["ana", "juan", "pedro", "maría", "luis", "sofia", "carlos", "lucia"]
nombreEliminado=""

while True:
    inputMenu=input("Seleccione una opción: \n 1. Mostrar nombres \n 2. Eliminar nombre \n 3. Salir \n")
    
    while inputMenu != "1" and inputMenu != "2" and inputMenu != "3":
        print("Opción inválida. Por favor, seleccione una opción válida.")
        inputMenu = input("Seleccione una opción: ")
        print("Menu de opciones: ")
        print("1. Mostrar nombres")
        print("2. Eliminar nombre")
        print("3. Salir")
    if inputMenu =="3":
        break
    elif inputMenu =="1":
        print(f"Los nombres de la lista son:")
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]}")
    elif inputMenu =="2":
        nombreEliminado=input("Ingrese el nombre que desea eliminar: ").lower()
        if nombreEliminado in nombres:
            nombres.remove(nombreEliminado)
            print(f"La lista actualizada de nombres es:")
            for i in range(len(nombres)):
                print(f"{i+1}. {nombres[i]} ")
        else:
            print("El nombre no se encuentra en la lista.")

------------------------------------------------
EJERCICIO 6     
lista = [3,5,7,9,11,13,15]
ultimo=lista[-1]
for i in range(len(lista)-1,0,-1):
    lista[i]=lista[i-1]
lista[0]=ultimo
print(lista)

------------------------------------------------
EJERCICIO 7

filas=7
columnas=2
matriz_temperaturas=[[0]*columnas for temperatura in range (filas)]
sumaMin=0
sumaMax=0
promedioMin=0
promedioMax=0
tempMin=0
tempMax=0
amplitud=0
mayorAmplitud=0
diaMayorAmplitud=0

print("Ingrese las temperaturas para la matriz")
for i in range(filas):
        tempMin=int(input(f"Ingrese la temperatura minima del dia {i+1}: "))
        tempMax=int(input(f"Ingrese la temperatura maxima del dia {i+1}: "))
        matriz_temperaturas[i][0]=tempMin
        matriz_temperaturas[i][1]=tempMax
        sumaMin+=matriz_temperaturas[i][0]
        sumaMax+=matriz_temperaturas[i][1]
        amplitud=tempMax-tempMin
        if amplitud>mayorAmplitud:
            mayorAmplitud=amplitud
            diaMayorAmplitud=i+1
        
promedioMin=sumaMin/filas
promedioMax=sumaMax/filas
print(f"El promedio de la minima en la semana fue: {promedioMin} mientras que el promedio de la maxima fue: {promedioMax}")
print(f"El día con mayor amplitud térmica fue el día {diaMayorAmplitud} con una amplitud de {mayorAmplitud}°C")
   

------------------------------------------------
EJERCICIO 8

estudiantes=5
materias=3
matriz_estudiantes=[[0]*materias for estudiante in range(estudiantes)]
sumaNotas=0
promedioEstudiante=0
promedioMateria=0
notas=0
sumaMaterias=0

print("Ingrese las notas: ")
for i in range(estudiantes):
    print(f"Estudiante {i+1}: ")
    for j in range(materias):
        notas=int(input(f"Ingrese la {j+1}° nota: "))
        matriz_estudiantes[i][j]=notas
        sumaNotas+=notas
    promedioEstudiante=sumaNotas/materias
    sumaNotas=0
    print(f"El promedio del estudiante {i+1} es {promedioEstudiante}")
for j in range(materias):
    for i in range(estudiantes):
        sumaMaterias+=matriz_estudiantes[i][j]
    promedioMateria=sumaMaterias/estudiantes
    print(f"El promedio de la materia {j+1} es: {promedioMateria}")
    sumaMaterias=0

-------------------------------- 
EJERCICIO 9
fila=-1
columna=-1
tablero=[["-"]*3 for _ in range(3)]
jugador="X"

while True:
    for fila in tablero:
        print("".join(fila))    
    fila=int(input(f"Ingrese la fila (0-2)"))
    columna=int(input(f"Ingrese la columna (0-2)"))
    if tablero[fila][columna]=="-":
        tablero[fila][columna]=jugador
    else:
        print("Casilla ocupada, elija otra")
        continue
    for fila in tablero:
        print("".join(fila))
    
    if jugador == "X":
        jugador="O"
    else:
        jugador="X"
--------------------------------
EJERCICIO 10 FALTA HACER TODAVIA

 Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
● Mostrar el total vendido por cada producto.
● Mostrar el día con mayores ventas totales.
● Indicar cuál fue el producto más vendido en la semana.


productos=4
dias=7
matriz_ventas=[[0]*productos for dia in range(dias)]
sumaProd=0
diaMayorVenta=0
sumaDia=0
mayor=0
dia=0
mayorProducto=0
producto=0

for i in range(dias):
    print(f"Dia {i+1}: ")
    for j in range(productos):
        ventasProd=int(input(f"Ingresa la cantidad de ventas del producto {j+1}: "))
        matriz_ventas[i][j]=ventasProd

for j in range(productos):
    print(f"Producto {j+1}")
    sumaProd=0
    for i in range(dias):
        sumaProd+=matriz_ventas[i][j]
    print(sumaProd)
        
for i in range(dias):
    sumaDia=0
    for j in range(productos):
        sumaDia+=matriz_ventas[i][j]
    if sumaDia>mayor:
        mayor=sumaDia
        dia=i+1
            
print(f"el dia con mayor venta fue el dia: {dia} con {mayor} ventas")

for j in range(productos):
    totalProductos=0
    for i in range(dias):
        totalProductos+=matriz_ventas[i][j]
    if totalProductos>mayorProducto:
        mayorProducto=totalProductos
        producto=j+1
print(f"El producto mas vendido en la semana fue el producto n°{producto}")

-------------------------------------
EJERCICIO 11

nombre=""
lista_nombres=["Juan","Alvaro","Sol","Lisandro","Pedro","Gustavo","Victoria","Ramon","Viena","Bernardo"]
nombre=input("Ingresa un nombre para buscar: ").capitalize()
if nombre in lista_nombres:
    indice=lista_nombres.index(nombre)
    print(f"{nombre} se encuentra en la lista")
    print(f"{nombre} es el {indice+1}° nombre en la lista")
else:
    print(f"{nombre} no se encuentra en la lista")

-------------------------------------
EJERCICIO 12
 
lista_numeros=[]
listaMayorMenor=[]
for i in range(8):
    user=int(input(f"Ingresa el {i+1}° numero entero para sumar a la lista: "))
    lista_numeros.append(user)
listaMayorMenor=sorted(lista_numeros)
listaReversa=sorted(lista_numeros,reverse=True)
    
print(f"La lista original es: {lista_numeros}")
print(f"La lista ordenada de menor a mayor es: {listaMayorMenor}")
print(f"La lista ordenada de mayor a menor es: {listaReversa}")

--------------------------------------
EJERCICIO 13

puntajes = [450, 1200, 875, 990, 300, 1500, 640]
mayor=puntajes[0]
menor=puntajes[0]
for i in puntajes:
    if i >= mayor:
        mayor=i
    if i<=menor:
        menor=i


mayorMenor=sorted(puntajes,reverse=True)
indice=mayorMenor.index(990)
print(f"El puntaje mas alto es: {mayor} mientras que el mas bajo es: {menor}")
print(f"Los puntajes ordenados de mayor a menor son los siguientes: {mayorMenor}")
print(f"990 se encuentra en la posicion {indice+1} del ranking")

"""