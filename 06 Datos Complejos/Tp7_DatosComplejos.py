""" #Ejercicio 1
precio_frutas={
    'Banana': 1200,
    'Anana': 2500,
    'Melon': 3000,
    'Uva': 1450
}
print(precio_frutas)
precio_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print(precio_frutas)

#Ejercicio 2
precio_frutas['Banana']=1330
precio_frutas['Manzana']=1700
precio_frutas['Melon']=2800
print(precio_frutas)

#Ejercicio 3
claves=precio_frutas.keys()
lista_claves= list(claves)
print(lista_claves)
#Ejercicio 4
agenda={}
for i in range(2):
    nombre=input(f"Ingresa el {i+1}° nombre: ")
    telefono=input(f"Ingresa el numero de la persona n° {i+1}: ")
    agenda[nombre]= telefono
busqueda=input("Ingresa un nombre para buscar: ")    
if busqueda in agenda:
    print(f"el numero de {busqueda} es: {agenda[busqueda]}")
else: 
    print(f"{busqueda} no existe.")
 #Ejercicio 5
frase=input("Ingresa una frase: ")
palabras=frase.split()
conjunto = set()
diccionario = {}
for palabra in palabras:
    conjunto.add(palabra)
    diccionario[palabra]=palabras.count(palabra)
print(f"Palabras unicas: {conjunto}")
print(f"Cantidad de veces: {diccionario}")
 """

 
    
