""" 
Ejercicio 1:
print("Hola mundo")
-------------------
ejercicio 2:
nombre=input("Ingresa tu nombre: ")
print(f"Hola {nombre}!") 
-------------------
Ejercicio 3:
nombre=input("Ingresa tu nombre: ")
apellido=input("Ingresa tu apellido: ")
domicilio=input("Ingresa tu domicilio: ")
print(f"Soy {nombre} {apellido} y vivo en {domicilio}.")
-------------------
Ejercicio 4:
import math
radio=float(input("Ingrese el radio del círculo: "))
area=math.pi*radio**2
perimetro=2*math.pi*radio
print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")
-------------------
Ejercicio 5:
segundos=int(input("Ingrese el tiempo en segundos: "))
horas=segundos//3600
print(f"El tiempo en horas es: {horas}")
-------------------
Ejercicio 6:
num=int(input("Ingrese un numero que desea ver la tabla de multiplicar: "))
for i in range(1, 11):
    resultado=num*i
    print(f"{num} x {i} = {resultado}") 
-------------------
Ejercicio 7:
num1=int(input("Ingrese el primer numero: "))
while num1==0:
    print("El numero no puede ser cero, ingrese otro numero.")
    num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
while num2==0:
    print("El numero no puede ser cero, ingrese otro numero.")
    num2=int(input("Ingrese el segundo numero: "))
resta=num1-num2
print(f"La resta de {num1} y {num2} es: {resta}")
suma=num1+num2
print(f"La suma de {num1} y {num2} es: {suma}")
multiplicacion=num1*num2
print(f"La multiplicacion de {num1} y {num2} es: {multiplicacion}")
division=num1/num2
print(f"La division de {num1} y {num2} es: {division:.2f}")
-------------------
Ejercicio 8:
peso=float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en metros: "))
imc=peso/altura**2
print(f"Su indice de masa corporal es: {imc:.2f}")
-------------------
Ejercicio 9:
celsius=float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit=(celsius*9/5)+32
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")
-------------------
Ejercicio 10:
"""
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
promedio=(num1+num2+num3)/3
print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
