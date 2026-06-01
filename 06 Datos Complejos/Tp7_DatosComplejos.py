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
palabras= frase.split()
conjunto=set()
diccionario={}
for palabra in palabras:
    conjunto.add(palabra)
    diccionario[palabra]=palabras.count(palabra)
print(f"Palabras unicas: {conjunto}")
print(f"Cantidad de veces: {diccionario}")
#Ejercicio 6
alumnos=[]
for i in range(3):
    nombre=input("Nombre: ")
    notas=[]
    for j in range(3):
        nota=int(input("Nota: "))
        notas.append(nota)
    notas=tuple(notas)
    alumno=(nombre, notas)
    alumnos.append(alumno)
print(alumnos)

#Ejercicio 7
asistencias=["Ana","Luis","Ana","Maria","Luis","Pedro","Ana"]
print(asistencias)
conjunto=set()
diccionario={}
for persona in asistencias:
    conjunto.add(persona)
    diccionario[persona]=asistencias.count(persona)
print(f"Personas unicas: {conjunto}")
print(f"Cantidad de veces: {diccionario}")

#Ejercicio 8
diccionario={
    "Papas": 240,
    "Sprite":300,
    "Mani":140,
    "Cerveza": 50
}
while True:
    print("Ingresa la opcion que desees: ")
    opcion=int(input("1. Consultar Stock | 2.Agregar un nuevo producto | 0.Salir: "))
    if opcion==1:
        selmenu=int(input("1. Consultar Stock | 2. Agregar Unidades: "))
        if selmenu==1:
            busqueda=input("Ingresa el nombre del producto: ").capitalize()
            if busqueda in diccionario:
                print(busqueda,diccionario[busqueda])
            else:
                print("El producto no existe")
        elif selmenu==2:
            busqueda=input("Ingresa el producto al que deseas agregar unidades: ").capitalize()
            if busqueda in diccionario:
                cantidad=int(input("Cuantos queres agregar? "))
                diccionario[busqueda]+=cantidad
                print(busqueda,diccionario[busqueda])

        else:
            print("Opcion fuera de rango.")
    
    elif opcion==2:
        print("Agregar producto: ")
        nuevo_producto=input("Ingresa el nombre del producto: ").capitalize()
        if nuevo_producto in diccionario:
            print("El producto ya existe.")
        else:
            cantidad_nuevo_producto=int(input("Ingresa la cantidad: "))
            diccionario[nuevo_producto]=cantidad_nuevo_producto
            print("Producto agregado correctamente")
        
    elif opcion==0:
        print("Saliendo...")
        break
    else:
        print("Opcion fuera de rango.")

        
#Ejercicio 9
agenda={
    ("Lunes","10:00"):"Reunion",
    ("Martes","09:00"):"Clase de ingles",
    ("Miercoles", "21:00"):"Futbol"
}
dia=input("Ingresa el dia para ver que hay en la agenda: ").capitalize()
hora=input("Ingresa la hora: ")
clave=(dia,hora)
if clave in agenda:
    print("Ocupado: ", agenda[clave])
else:
    print("No tienes nada en la agenda")
 """

#Ejercicio 10
paises={
    "Argentina":"Buenos aires",
    "Chile": "Santiago",
    "Peru": "Lima"
}
invertido={}
for pais,capital in paises.items():
    invertido[capital]=pais
print(paises)
print(invertido)



