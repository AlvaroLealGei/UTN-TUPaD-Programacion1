""" 
EJERCICIO 1

edad = int(input("¿Cuál es tu edad? "))
if edad > 18:
    print("Eres mayor de edad.") 
    -----------------------------
EJERCICIO 2

nota = int(input("¿Cuál es tu nota? "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    -----------------------------
EJERCICIO 3

numero = int(input("Ingrese un número : "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("Por favor, ingrese un número par.")
    ------------------------------
EJERCICIO 4

numero = int(input("Ingrese un número: "))
if numero < 12:
    print(f"Tienes {numero} años, eres un niño.")
elif numero >= 12 and numero <18:
    print(f"Tienes {numero} años, eres un adolescente.")
elif numero >=18 and numero <30:
    print(f"Tienes {numero} años, eres un adulto joven.")
else:
    print(f"Tienes {numero} años, eres un adulto.")
    -------------------------------
EJERCICIO 5
   
contra = input("Ingrese su contraseña: ")
if len(contra) >= 8 and len(contra) <= 14:
    print("Ha ingresado una contraseña válida.")
else:    print("La contraseña debe tener entre 8 y 14 caracteres.") 
    -------------------------------
EJERCICIO 6

kw = int(input("Ingrese la cantidad de kilovatios consumidos: "))
if kw <= 150:
    print("Consumo bajo")
elif kw >= 150 and kw <= 300:
    print("Consumo medio")
elif kw > 500:
    print("Considere medidas de ahorro energético")
else:    print("Consumo alto")
    -------------------------------
EJERCICIO 7

str = input("Ingrese una palabra: ")
if str[-1] == "a" or str[-1] == "e" or str[-1] == "i" or str[-1] == "o" or str[-1] == "u":
    print(f"{str}!")
else: print(str)
    -------------------------------
EJERCICIO 8

nm = input("Ingresa ya sabes que:")
nb=int(input("Ingresa 1 si lo deseas en MM, 2 si lo deseas en mm y 3 si lo deseas en Mm:"))
if nb==1:
    print(f"{nm.upper()}")
elif nb==2:    print(f"{nm.lower()}")
elif nb==3:    print(f"{nm.capitalize()}")
else: print("Opción no válida")
    -------------------------------
EJERCICIO 9

magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3.0:
   print("Muy leve") 
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Leve")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy Fuerte")
else: print ("Extremo")
--------------------
EJERCICIO 10

hmfr=input("En que hemisferio te encuentras? S/N").lower()
mes=input("En que mes te encuentras?").lower()
dia=input("que dia del mes es?")

if hmfr=="s":
    if mes == "diciembre" and dia >=21 or mes == "enero" or mes =="febrero" or mes == "marzo" and dia <=20:
        print("Estás en verano")
    elif mes =="marzo" and dia >=21 or mes =="abril" or mes =="mayo" or mes =="junio" and dia <=20:
        print("Estás en otoño")
    elif mes =="junio" and dia >=21 or mes =="julio" or mes =="agosto" or mes =="septiembre" and dia <=20:
        print("Estás en invierno")
    elif mes =="septiembre" and dia >=21 or mes =="octubre" or mes =="noviembre" or mes =="diciembre" and dia <=20:
        print("Estás en primavera")
elif hmfr=="n":
    if mes == "diciembre" and dia >=21 or mes == "enero" or mes =="febrero" or mes == "marzo" and dia <=20:
        print("Estás en invierno")
    elif mes =="marzo" and dia >=21 or mes =="abril" or mes =="mayo" or mes =="junio" and dia <=20:
        print("Estás en primavera")
    elif mes =="junio" and dia >=21 or mes =="julio" or mes =="agosto" or mes =="septiembre" and dia <=20:
        print("Estás en verano")
    elif mes =="septiembre" and dia >=21 or mes =="octubre" or mes =="noviembre" or mes =="diciembre" and dia <=20:
        print("Estás en otoño")

"""

