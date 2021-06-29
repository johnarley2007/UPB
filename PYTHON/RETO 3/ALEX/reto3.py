from os import system
import os
import time
import random
system("clear")

x = 51661
y = 16615
coordenada = []

def ingresarCoordenada (coordenadaInicial):
    coordenadaDuplicada = list(coordenadaInicial)
    for x in range (0,3):
        coordenadaDuplicada.append([])
        lat = input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            print("Error")
            exit()
        lat = float(lat)
        if lat <= 5.413 and lat >= 5.119:
            lon = input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                print("Error")
                exit()
            lon = float(lon)
            if lon <= -76.132 and lon >= -76.619:
                coordenadaDuplicada[x].insert(0,lat)
                coordenadaDuplicada[x].insert(1,lon)
            else:
                print("Error coordenada")
                exit()
        else:
            print("Error coordenada")
            exit()
    print("Coordenadas ingresadas correctamente")
    time.sleep(2)
    return coordenadaDuplicada

def ordenarLatitudes(coordenadaInicial):
    print(f"La coordenada que está mas al sur es: {min(coordenadaInicial, key=lambda posicion:posicion[0])}")
    print(f"La coordenada que está mas al norte es: {max(coordenadaInicial, key=lambda posicion:posicion[0])}")

def ordenarLongitudes(coordenadaInicial):
    print(f"La coordenada que está mas al oriente es: {max(coordenadaInicial, key=lambda posicion:posicion[1])}")
    print(f"La coordenada que está mas al occidente es: {min(coordenadaInicial, key=lambda posicion:posicion[1])}")

def promedioCoordenadas(coordenadaInicial):
    print(f"El promedio de las latitudes es: {(coordenadaInicial[0][0]+coordenadaInicial[1][0]+coordenadaInicial[2][0])/3}")
    return
    print(f"El promedio de las longitudes es: {(coordenadaInicial[0][0]+coordenadaInicial[0][1]+coordenadaInicial[0][2])/3}")

def imprimirCoordenada(coordenadaInicial):
    coordenadaDuplicada=list(coordenadaInicial)
    print("Las coordenadas guardadas actualmente son:")
    for x in range(0,len(coordenadaDuplicada)):
        print(f"{x+1}. Coordenada Latitud:'{coordenadaDuplicada[x][0]}' Longitud: ' {coordenadaDuplicada[x][1]}'")
    ordenarLatitudes(coordenadaDuplicada)
    ordenarLongitudes(coordenadaDuplicada)
    promedioCoordenadas(coordenadaDuplicada)
    choice=int(input("Por favor ingrese la opción que desea modificar"))
    if choice!=1 and choice!=2 and choice!=3:
        print("Error actualización")
        exit()
    else:
        actualizarCoordenadas(choice,coordenadaInicial)

def actualizarCoordenadas(choice, coordenadaInicial):
    coordenadaDuplicada = list(coordenadaInicial)
    choice=choice-1
    lat = input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
        print("Error")
        exit()
    lat = float(lat)
    if lat <= 5.413 and lat >= 5.119:
        lon = input("Ingrese la longitud: ")
        while lon == "" or lon == " ":
            print("Error")
            exit()
        lon = float(lon)
        if lon <= -76.132 and lon >= -76.619:
            coordenadaDuplicada[choice][0]=lat
            coordenadaDuplicada[choice][1]=lon
        else:
            print("Longitud fuera del rango")
            coordenadaDuplicada=[coordenadaInicial] #En caso de error retornamos la lista original (sin cambios)
            return coordenadaDuplicada
    else:
        print("Latitud fuera del rango")
        coordenadaDuplicada=[coordenadaInicial] 
        return coordenadaDuplicada
    
    return coordenadaDuplicada #En caso éxito retornamos la nueva lista


print("Bienvenido al sistema de ubicación para zonas públicas WIFI”")
usuario = int(input("Digite el usuario: "))
if usuario == x:
    system("clear")
    contraseña = int(input("Digite la contraseña: "))
    if contraseña == y:
        system("clear")
        termino1=661
        termino2=(2*1)+5-1
        captcha = str(print(termino1," + ",termino2,"=",))
        valor=str(input())
        if valor==str((termino1+termino2)):
            system("clear")
            print("Sesión iniciada")
            menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión."]
            cont = 0
            while True:
                if cont >= 3:
                    print ("Error")
                    exit()
                for i in range(7):
                    print(str(i+1),". ",menu[i])
                try:
                    opcion = int(input("Elija una opción"))
                    if opcion < 1 or opcion > 7:
                        print("Error")
                        cont += 1
                    elif opcion == 1:
                        claveAnterior = int(input("Digite la contraseña anterior: "))
                        if y != claveAnterior:
                            print("Error")
                            exit()
                        else:    
                            nuevaClave = int(input("Digite la nueva contraseña: "))
                            while nuevaClave == y:
                                print("Error")
                                nuevaClave = int(input("Digite la nueva contraseña: "))    
                            nuevaClave2 = int(input("Confirmar nueva contraseña: "))
                            if nuevaClave == nuevaClave2:
                                y = nuevaClave
                                print("Cambio de contraseña exitoso")
                            else:
                                print("Error")
                    elif opcion == 2:
                        if coordenada==[]:
                            coordenada = ingresarCoordenada(coordenada)
                        else:
                            imprimirCoordenada(coordenada)
                    elif opcion == 6:
                        try:
                            favorita = int(input("Seleccione opción favorita"))
                            cont = 0
                            if favorita < 1 or favorita > 5:
                                print("Error")
                                exit()
                            else:
                                try:
                                    digito1 = int(input("Cantidad esquinas de un triángulo: "))
                                    if digito1 == 3:
                                        digito2 = int(input("Cuantos lados tiene un cuadrado:"))
                                        if digito2 == 4:
                                            favorita -= 1
                                            temporal = menu[favorita]
                                            menu.pop(favorita)
                                            menu.insert(0,temporal)
                                        else:
                                            print("Error")
                                    else:
                                        print("Error")
                                except ValueError:
                                    print("Error")
                        except ValueError:
                            print("Error")
                            exit()
                    elif opcion >=1 and opcion <=5:
                            print ("Usted ha elegido la opción "+str(opcion)+"")
                            exit()
                    elif opcion == 7:
                        print("Hasta pronto")
                        exit()
                except ValueError:
                    print("Error")
                    cont += 1
        else:
            system("clear")
            print("Error")
    else:
        system("clear")
        print("Error")
else:
    system("clear")
    print("Error")