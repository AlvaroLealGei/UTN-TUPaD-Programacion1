
"""Ejercicio integrador - Caja del kiosconombre = input("Cual es tu nombre? ")
while not nombre.isalpha():
    print("Debes ingresar al menos una letra. El nombre no puede contener numeros o caracteres especiales")
    nombre = input("Cual es tu nombre? ")
cantProductos = (int(input("Cuantos productos quieres comprar? ")))
while cantProductos== 0:
    print("Intente nuevamente, no se pueden comprar 0 productos")
    cantProductos = (int(input("Cuantos productos quieres comprar? ")))
while cantProductos < 0:
    print("La cantidad de productos debe ser un numero positivo")
    cantProductos = (int(input("Cuantos productos quieres comprar? ")))


resumen=f"Cliente: {nombre}\nCantidad de productos: {cantProductos} \n"

ahorroTotal=0
promedioPorProducto=0
totalSinDescuento=0
totalConDescuento=0
sumaPromedio=0

for i in range(int(cantProductos)):
    print("Producto ", i + 1)
    
    
    precioOriginal = input(f"Ingrese el precio del producto {i + 1}: ")
    
    while precioOriginal.isdigit() == False:
        print("El precio del producto debe ser un numero")
        precioOriginal = input(f"Ingrese el precio del producto {i + 1}: ")
    descuento=input(f"El producto {i+1} tiene descuento? (s/n) ")
        
    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Ingrese s para si o n para no")
        descuento=input(f"El producto {i+1} tiene descuento? (s/n) ")
    if descuento.lower() == "s":
        precioFinal = float(precioOriginal) * 0.9
    else:
        precioFinal = float(precioOriginal)
        
    precioOriginal = float(precioOriginal)
    totalConDescuento= totalConDescuento + precioFinal
    totalSinDescuento= totalSinDescuento + precioOriginal
    ahorroTotal= ahorroTotal + (precioOriginal - precioFinal)
    sumaPromedio+= precioFinal
    
    resumen+=f"Producto {i+1} - Precio: {precioFinal:.2f} - Descuento: {'Si' if descuento.lower() == 's' else 'No'}\n"
    
promedioPorProducto= sumaPromedio/cantProductos
    
print(resumen)
print(f"Total sin descuento: {totalSinDescuento:.2f} \nTotal con descuento: {totalConDescuento:.2f} \nAhorro total: {ahorroTotal:.2f} \nPromedio por producto: {promedioPorProducto:.2f}")"""

"""EJERCICIO 2 - ACCESO AL CAMPUS Y MENU SEGURO"""
"""user = "alumno"
password = "python123"
for i in range(3):
    userInput = input("Ingresa tu usuario: ")
    passwordInput = input("Ingresa tu contraseña: ")
    intentoUser = i+1
    if userInput == user and passwordInput == password:
        print(
            f"Intento {intentoUser}/3 - Usuario: {userInput}\nClave: {passwordInput}\nAcceso concedido")

        inputMenu = ""
        while inputMenu != "4":
            print(
                "1. Ver estado de inscripcion\n2. Cambiar contraseña\n3. Mostrar mensaje motivacional\n4. Salir")

            inputMenu = input(
                "Ingrese el numero de la opcion que desea realizar: ")
            
            while not inputMenu.isdigit():
                print("Error, opcion fuera de rango")
                inputMenu = input(
                    "Ingrese el numero de la opcion que desea realizar: ")
                while inputMenu != "1" and inputMenu != "2" and inputMenu != "3" and inputMenu != "4":
                    print("Error, opcion fuera de rango")
                    inputMenu = input(
                        "Ingrese el numero de la opcion que desea realizar: ")
            if inputMenu == "1":
                print("Estado de inscripcion: Inscripto")
            elif inputMenu == "2":
                newPassword = input("Ingrese su nueva contraseña: ")
                while True:
                    newPassword = input("Ingrese su nueva contraseña: ")
                    if newPassword == "" or len(newPassword) < 6:
                        print(
                            "La contraseña no puede estar vacia y debe tener al menos 6 caracteres")
                        continue
                    confirmPassword = input("Confirme su nueva contraseña: ")
                    if newPassword == confirmPassword:
                        password = newPassword
                        print("Contraseña cambiada exitosamente")
                        break
                    else:
                        print("Las contraseñas no coinciden, intente nuevamente")

            elif inputMenu == "3":
                print("Segui estudiando, vos podes!!")
            elif inputMenu == "4":
                break

    else:
        print(
            f"\nIntento {intentoUser}/3 - Usuario: {userInput}\nClave: {passwordInput}\nError, credenciales inválidas")
else:
    print("\nCuenta bloqueada")
"""

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
"""lunes = 4
martes = 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")
while operador.isalpha() == False:
    print("El nombre del operador debe contener solo letras")
    operador = input("Ingrese el nombre del operador: ")
while True:
    print("1.Reservar turno")
    print("2.Cancelar turno")
    print("3.Ver agenda del dia")
    print("4.Ver resumen general")
    print("5.Cerrar sistema")
    selMenu = input("Seleccione una opcion: ")
    while not selMenu.isdigit():
        print("Error, opcion fuera de rango")
        selMenu = input("Seleccione una opcion: ")
    while selMenu != "1" and selMenu != "2" and selMenu != "3" and selMenu != "4" and selMenu != "5":
        print("Error, opcion fuera de rango")
        selMenu = input("Seleccione una opcion: ")
        
    if selMenu == "1":
        dia = input("Elegi el dia Lunes-1 Martes-2")
        while not dia.isdigit() or (dia != "1" and dia != "2"):
            print("Dia invalido, intente nuevamente")
            dia = input("Elegi el dia Lunes-1 Martes-2")
        paciente = input("Ingrese el nombre del paciente: ")
        while not paciente.isalpha():
            print("El nombre del paciente debe contener solo letras")
            paciente = input("Ingrese el nombre del paciente: ")
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno reservado para el lunes")
            else:
                if lunes == "":
                    lunes1 = paciente
                elif lunes2=="":
                    lunes2 = paciente
                elif lunes3=="":
                    lunes3 = paciente
                elif lunes4=="":
                    lunes4 = paciente
                else:
                    print("No hay turnos disponibles para el lunes")
        elif dia == "2":
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno reservado para el martes")
            else:
                if martes1 == "":
                    martes1 = paciente
                elif martes2=="":
                    martes2 = paciente
                elif martes3=="":
                    martes3 = paciente
                else:
                    print("No hay turnos disponibles para el martes")
    elif selMenu == "2":
        dia =input("Elegi el dia Lunes-1 Martes-2")
        paciente = input("Ingrese el nombre del paciente: ")
        while not paciente.isalpha():
            print("El nombre del paciente debe contener solo letras")
            paciente = input("Ingrese el nombre del paciente: ")
        if dia == "1":
            if paciente == lunes1:
                lunes1 = ""
            elif paciente == lunes2:
                lunes2 = ""
            elif paciente == lunes3:
                lunes3 = ""
            elif paciente == lunes4:
                lunes4 = ""
            else:
                print("El paciente no tiene un turno reservado para el lunes")
        elif dia == "2":
            if paciente == martes1:
                martes1 = ""
            elif paciente == martes2:
                martes2 = ""
            elif paciente == martes3:
                martes3 = ""
            else:
                print("El paciente no tiene un turno reservado para el martes")
    elif selMenu == "3":
        dia = input("Elegi el dia Lunes-1 Martes-2")
        if dia == "1":
            print("Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 != '' else 'libre'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else 'libre'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else 'libre'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else 'libre'}")
        elif dia == "2":
            print("Martes:")
            print(f"Turno 1: {martes1 if martes1 != '' else 'libre'}")
            print(f"Turno 2: {martes2 if martes2 != '' else 'libre'}")
            print(f"Turno 3: {martes3 if martes3 != '' else 'libre'}")
    elif selMenu == "4":
        ocupadosLunes=0
        ocupadosMartes=0
        if lunes1!="":
            ocupadosLunes+=1
        if lunes2 != "":
            ocupadosLunes+=1
        if lunes3!="":
            ocupadosLunes+=1
        if lunes4 !="":
            ocupadosLunes+=1
        
        if martes1!="":
            ocupadosMartes+=1
        if martes2!="":
            ocupadosMartes+=1
        if martes3!="": 
            ocupadosMartes+=1
        print(f"Resumen:\n")
        print(f"Lunes: {ocupadosLunes} turnos ocupados, {4-ocupadosLunes} turnos libres")
        print(f"Martes: {ocupadosMartes} turnos ocupados, {3-ocupadosMartes} turnos libres")
        
        if ocupadosLunes > ocupadosMartes:
            print("El dia mas ocupado es el lunes")
        elif ocupadosMartes > ocupadosLunes:
            print("El dia mas ocupado es el martes")
        else: 
            print("Ambos dias tienen la misma cantidad de turnos ocupados")
                    
    elif selMenu == "5":
        print("Cerrando sistema...")
        break
"""

# Ejercicio 4 — “Escape Room: La Bóveda”
"""import random
import string
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
riesgoAlarma = ""
intentosSeguidos = 0

nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    print("El nombre debe contener solo letras")
    nombre = input("Ingrese su nombre: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print(f"Agente: {nombre} - Energia: {energia} - Tiempo restante: {tiempo} - Cerraduras abiertas: {cerraduras_abiertas}")
    print("1- Forzar cerradura 2- Hackear Panel 3- Descansar")
    opcion = input("Seleccione una opcion: ")
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        print("Opcion invalida, intente nuevamente")
        opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        energia -= 20
        tiempo -= 2
        intentosSeguidos += 1
        if energia < 40:
            riesgoAlarma = input("Riesgo de alarma. Elija un numero de 1 a 3")
            while not riesgoAlarma.isdigit() or (riesgoAlarma != "1" and riesgoAlarma != "2" and riesgoAlarma != "3"):
                print("Opcion invalida, intente nuevamente")
                riesgoAlarma = input(
                    "Riesgo de alarma. Elija un numero de 1 a 3")
            if riesgoAlarma == "1":
                cerraduras_abiertas += 1
            elif riesgoAlarma == "2":
                cerraduras_abiertas += 1
            elif riesgoAlarma == "3":
                alarma = True
        if intentosSeguidos == 3:
            print("Has forzado la cerradura 3 veces seguidas, la alarma se ha activado")
            alarma = True
            break
    elif opcion == "2":
        energia -= 10
        tiempo -= 3
        intentosSeguidos=0
        for i in range(1,5):
            letra=random.choice(string.ascii_uppercase)
            codigo_parcial += letra
            print(f"Hackeando {i}/4")
            print(f"Codigo parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura hackeada exitosamente")   
    elif opcion == "3":
        energia += 15
        tiempo -= 1
        intentosSeguidos = 0
        if alarma:
            energia -= 10
            
if alarma == True and tiempo <=3 and cerraduras_abiertas < 3:
    print("La alarma se ha activado, has sido atrapado")
if cerraduras_abiertas == 3:
    print("Felicidades, has abierto las 3 cerraduras y escapado de la bóveda")
elif energia <= 0 or tiempo <= 0:
    print("Has quedado sin energia o se ha agotado el tiempo, has sido atrapado")
elif alarma == True:
    print("La alarma se ha activado, has sido atrapado")
             
"""


vidaGladiador=100
vidaEnemigo=100
pocionesVida=3
ataquePesado=15
golpeCritico=ataquePesado*1.5
ataqueRafaga=5
ataqueEnemigo=12
turnoGladiador=True
print("----BIENVENIDO A LA ARENA----")
gladiador=input("Ingrese el nombre del gladiador: ")
while not gladiador.isalpha():
    print("El nombre del gladiador debe contener solo letras")
    gladiador=input("Ingrese el nombre del gladiador: ")
print(f"Nombre del gladiador {gladiador}")
print("=== INICIO DEL COMBATE ===")
while vidaGladiador > 0 and vidaEnemigo > 0:
    while turnoGladiador:
        print(f"{gladiador} ({vidaGladiador} HP) vs Enemigo: ({vidaEnemigo} HP) | Pociones: {pocionesVida}")
        print("Elije accion:")
        opcion=input("1- Ataque Pesado\n2- Ráfaga Veloz\n3- Curar\n")
        while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
            print("Opcion invalida, intente nuevamente")
            opcion = input("Seleccione una opcion: ")
        print(f"Opcion: {opcion}")
        if opcion == "1":
            if vidaEnemigo < 20:
                vidaEnemigo-=golpeCritico                
                print(f"Golpe critico! \nAtacaste al enegigo por {golpeCritico} puntos de daño!")
                turnoGladiador=False
            else:
                vidaEnemigo -= ataquePesado
                print(f"Atacaste al enemigo por {ataquePesado} puntos de daño")
                turnoGladiador=False
        elif opcion =="2":
            for i in range(3):
                vidaEnemigo -= ataqueRafaga
                print(f">Golpe conectado por {ataqueRafaga} de daño")
            turnoGladiador=False
        elif opcion=="3":
            if pocionesVida ==0:
                print("No te queda pociones")
                turnoGladiador=False
            else:
                vidaGladiador += 30
                pocionesVida -=1
                turnoGladiador=False
    vidaGladiador-=ataqueEnemigo
    print(f"El enemigo contraataca por {ataqueEnemigo} puntos de daño")
    turnoGladiador=True
    print("NUEVO TURNO")
if vidaGladiador>0:
    print(f"VICTORIA! {gladiador} has ganado la batalla")
else:
    print(f"DERROTA! {gladiador} ha sido derrotado por el enemigo")
      