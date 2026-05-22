import math

#Ejercicio 1
def hola_mundo():
    print("Hola mundo")

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Ejercicio 4
def calcular_area_circulo(radio):
    area= math.pi * (radio ** 2)
    print(area)
def calcular_perimetro_circulo(radio):
    perimetro= 2 * (math.pi * radio)
    print(perimetro)
#Ejercicio 5
def segundos_a_horas(segundos):
    hora=segundos/3600
    print(hora)
#Ejercicio 6
def tabla_multiplicar(num):
    for i in range (1,11):
        print(f"{num} x {i} = {num*i}")
    
#Ejercicio 7
def operaciones_basicas(a,b):
    operaciones=["Suma","Resta","Multiplicacion","Division"]
    resultados=[]
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    resultados.append(suma)
    resultados.append(resta)
    resultados.append(multiplicacion)
    resultados.append(division)
    print(operaciones)
    print(resultados)

#Ejercicio 8
def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    print(imc)
    
#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit= (celsius * 9 / 5) + 32
    print(fahrenheit)
    
#Ejercicio 10
def calcular_promedio(a,b,c):
    promedio= (a + b + c)/3
    print(f"El promedio es: {promedio}.")
    
#Programa Principal

#hola_mundo()
#nombre=input("Ingresa tu nombre: ")
#saludar_usuario(nombre)
#nombre=input("Ingresa tu nombre: ")
#apellido=input("Ingresa tu apellido: ")
#edad=input("Ingresa tu edad: ")
#residencia=input("Ingresa tu residencia: ")
#informacion_personal(nombre,apellido, edad, residencia)
#radio=int(input("Ingresa el radio del area: "))
#calcular_area_circulo(radio)
#calcular_perimetro_circulo(radio)
#segundos=int(input("Ingresa la cantidad de segundos para ver en horas"))
#segundos_a_horas(segundos)
#num=int(input("Ingrese un numero para vere su tabla"))
#tabla_multiplicar(num)
#a=int(input("Ingrese el primer numero: "))
#b=int(input("Ingrese el segundo numero: "))
#operaciones_basicas(a,b)
#peso=int(input("Ingresa tu peso en kg: "))
#altura=float(input("Ingresa tu altura en metros: "))
#calcular_imc(peso,altura)
#celsius=float(input("Ingresa la temperatura en celsius para ver el equivalente en fahrenheit: "))
#celsius_a_fahrenheit(celsius)
a=int(input("Ingresa el primer numero"))
b=int(input("Ingresa el segundo numero"))
c=int(input("Ingresa el tercer numero"))
calcular_promedio(a,b,c)



