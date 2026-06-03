"""
#Ejercicio 1
a=10
b=input("Introduce un numero: ") 

result=a/b #Error TypeError 'b' es un str mientras que 'a' es un int y no permite la division
print(f"Resultado: {result}")

numbers=[1,2,3]
print(numbers[5]) #Error IndexError, se esta pidiendo que se imprima un indice que no se encuentra en la lista

#Ejercicio 2
a=10
b=input("Introduce un numero: ")
while not b.isdigit():
    print("Error, debe ingresar un numero")
    b=input("Introduce un numero: ")
b=int(b)
result=a/b
print(result)

#Ejercicio 3
try:
    a = 10
    b = input("Introduce un numero: ")

    result = a / b  # Genera TypeError porque b es string
    print(f"Resultado: {result}")

except TypeError:
    print("Error: no se puede dividir un entero por una cadena de texto.")

numbers = [1, 2, 3]

try:
    print(numbers[5])  # Genera IndexError
except IndexError:
    print("Error: el índice solicitado no existe en la lista.")

#Ejercicio 4
# Error TypeError

try:
    a = 10
    b = input("Introduce un numero: ")

    result = a / b
    print(f"Resultado: {result}")

except TypeError:
    print("Error de tipo: no se puede dividir un entero por una cadena de texto.")

# Error IndexError

try:
    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:
    print("Error de índice: la posición solicitada no existe en la lista.")

#Ejercicio 5
# Error TypeError

try:
    a = 10
    b = input("Introduce un numero: ")

    result = a / b
    print(f"Resultado: {result}")

except TypeError:
    print("Error de tipo: no se puede dividir un entero por una cadena de texto.")

else:
    print("La operación se realizó correctamente.")

finally:
    print("Fin del bloque de división.")

# Error IndexError

try:
    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:
    print("Error de índice: la posición solicitada no existe en la lista.")

else:
    print("El índice existe y se mostró correctamente.")

finally:
    print("Fin del bloque de acceso a la lista.")# Error IndexError

try:
    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:
    print("Error de índice: la posición solicitada no existe en la lista.")

else:
    print("El índice existe y se mostró correctamente.")

finally:
    print("Fin del bloque de acceso a la lista.")
#Ejercicio 6
try:
    entrada = int(input("Ingresa un numero: "))
except ValueError:
    print("Debes ingresar un valor numerico.")
except Exception as e:
    print(f"Error inesperado: {type(e).__name__}")
else:
    print(entrada)
"""
#Ejercicio 7

while (True):
    try:
        entrada = int(input("Ingresa un numero: "))
    except ValueError:
        print("Debes ingresar un valor numerico.")
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}")
    else:
        print(entrada)
        break

