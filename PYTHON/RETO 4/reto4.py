from os import system
import os
import time
import random
from math import asin,cos,sin,sqrt,radians,degrees
system("clear")

x = 51661
y = 16615
coordenada = []
listadistancias=[]
radio=6372.795477598
restauranteactual=None
distanciaparatiempo=None
listacoordenadaspredet=[[5.273,-76.579,390],
                        [5.311,-76.413,333],
                        [5.354,-76.204,240],
                        [5.306,-76.332,793]]

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
#RETO4
def MostrarRestaurantesFav(coordenadaInicial):
    if coordenadaInicial==[]:
        print("Error sin registro de coordenadas")
        exit()
    else:
        ImprimirRestauratesFav(coordenadaInicial)

def ImprimirRestauratesFav(coordenadaInicial):
    coordenadaDuplicada = list(coordenadaInicial)
    print("Las coordenadas guardadas actualmente son: ")

    for x in range(0,len(coordenadaDuplicada)):
        print(f"{x+1}. Coordenada Latitud:'{coordenadaDuplicada[x][0]}' Longitud: ' {coordenadaDuplicada[x][1]}'")
        opcion=int(input("Por favor seleccione su restaurante actual: "))
        if opcion == 1 or opcion ==2 or opcion ==3:
            global restauranteactual
            restauranteactual=coordenada[opcion-1]
            PrepararDatos(opcion,coordenadaDuplicada,listacoordenadaspredet)
        else:
            print("Error ubicación")
            exit()

def PrepararDatos(IndRestauranteactual,coordenadaInicial,coordenadasfijas):
    coordenadaDuplicada=list(coordenadaInicial)
    listaduplicadafijas=list(coordenadasfijas)
    lat1=coordenadaDuplicada[IndRestauranteactual-1][0]
    lon1=coordenadaDuplicada[IndRestauranteactual-1][1]
    lat1=convertiraRadianes(lat1)
    lon1=convertiraRadianes(lon1)

    for x in range(0,len(listaduplicadafijas)):
        for y in range (0,2):
           
            listaduplicadafijas[x][y]=convertiraRadianes(listaduplicadafijas[x][y])
    
    AplicarFormulaDistancia(lat1,lon1,listaduplicadafijas)
    
    pass

def convertiraRadianes(valoraconvertir):
    return radians(valoraconvertir)
    pass

def AplicarFormulaDistancia(lat1, lon1, listaenradianes):

    
    for x in range(0,4):
        lat2=listaenradianes[x][0]
        lon2=listaenradianes[x][1]
        latdelta=lat2-lat1
        londelta=lon2-lon1

        auxiliarcalculo=sin(londelta/2)**2
        auxiliarcalculo=auxiliarcalculo*(cos(lat1)*cos(lat2))
        auxiliarcalculo=(sin(latdelta/2)**2)+auxiliarcalculo
        auxiliarcalculo=sqrt(auxiliarcalculo)
        auxiliarcalculo=asin(auxiliarcalculo)
        auxiliarcalculo=(2*radio)*auxiliarcalculo

        auxiliarcalculo=auxiliarcalculo*1000
        auxiliarcalculo=round(auxiliarcalculo)
       
        listadistancias.append(auxiliarcalculo)

    OrdenarDistancias(listadistancias)

def OrdenarDistancias(distancias):
    distanciasduplicadas=list(distancias)
    min1=distanciasduplicadas.index(min(distanciasduplicadas)) 
    distanciasduplicadas.pop(min1)
   
    min2=distancias.index(min(distanciasduplicadas))
               
    
    ImprimirMensajeCercanias(min1,min2,listacoordenadaspredet,distancias)

def ImprimirMensajeCercanias(min1,min2, basededatos,listadistancias ):
    for x in range (0,4):
        basededatos[x][0]=degrees(basededatos[x][0])
        basededatos[x][1]=degrees(basededatos[x][1])
    

    for x in range (0,len(listacoordenadaspredet)):
        if listacoordenadaspredet[min1][0]==listacoordenadaspredet[x][0] and listacoordenadaspredet[min1][1] == listacoordenadaspredet[x][1]:
            if listacoordenadaspredet[x][2]>listacoordenadaspredet[min1][2]:
                min1=listacoordenadaspredet.index(listacoordenadaspredet[x])
                

    global distanciaparatiempo 
    if basededatos[min1][2] > basededatos[min2][2]:
        
        print(f"1. El restaurante más cercano está en la latitud: '{basededatos[min1][0]}' longitud: '{basededatos[min1][1]}', está a {listadistancias[min1]} metros, y tiene {basededatos[min1][2]} platos.")
        print(f"2. El segundo restaurante más cercano está en la latitud: '{basededatos[min2][0]}' longitud: '{basededatos[min2][1]}', está a {listadistancias[min2]} metros, y tiene {basededatos[min2][2]} platos.")
        opcdestino=int(input("Por favor seleccione el restaurante al cual desea ir, para recibir indicaciones: "))
        if opcdestino==1: 
            distanciaparatiempo = listadistancias[min1] 
            DarIndicaciones(restauranteactual,basededatos[min1])
        elif opcdestino==2:
            distanciaparatiempo = listadistancias[min2]
            DarIndicaciones(restauranteactual,basededatos[min2])
        else:
            print("Error zona wifi")
            exit()
        
    else:
        print(f"1. El restaurante más cercano está en la latitud: '{basededatos[min2][0]}' longitud: '{basededatos[min2][1]}', está a {listadistancias[min2]} metros, y tiene {basededatos[min2][2]} platos.")
        print(f"2. El segundo restaurante más cercano está en la latitud: '{basededatos[min1][0]}' longitud: '{basededatos[min1][1]}', está a {listadistancias[min1]} metros, y tiene {basededatos[min1][2]} platos.")
        opcdestino=int(input("Por favor seleccione el restaurante al cual desea ir, para recibir indicaciones: "))
        if opcdestino==1:
            distanciaparatiempo= listadistancias[min2]
            DarIndicaciones(restauranteactual,basededatos[min2])
        elif opcdestino==2:
            distanciaparatiempo= listadistancias[min1]
            DarIndicaciones(restauranteactual,basededatos[min1])
        else:
            print("Error zona wifi")
            exit()

def DarIndicaciones(restactual,restdestino):

    latorigen=restactual[0]
    lonorigen=restactual[1]
    latdestino=restdestino[0]
    londestino=restdestino[1]

    if latorigen>latdestino:
        txt1="el sur"
    elif latorigen<latdestino:
        txt1="el norte"

    else:
        txt1=""
     
 
    if lonorigen>londestino:
        txt2="el occidente"
    elif lonorigen<londestino:
        txt2="el oriente"
    else:
        txt2=""
    

    if txt1=="" and txt2!="": 
        print(f"Debe ir hacia {txt2}")

    elif txt2=="" and txt1!="": 
        print(f"Debe ir hacia {txt1}")

    elif txt1=="" and txt2=="":
        print("Usted ya está en el destino")
        time.sleep(3)
        

    else:
        print(f"Debe dirigirse primero hacia {txt1} y luego hacia {txt2}")
        
        time.sleep(2)
        CalcularTiempoRecorrido()    
   
def CalcularTiempoRecorrido():
    tiempo1="segundos" 
    tiempo2="segundos"
    
    if distanciaparatiempo==0: 
        pass
        
    else:
        auto=distanciaparatiempo/16.67
        moto=distanciaparatiempo/0.483
        
        if auto > 60: 
            auto=auto/60
            tiempo1="minutos"
        
        
        if moto > 60:
            moto=moto/60
            tiempo2="minutos"
        
        moto=round(moto,2) 
        auto=round(auto,2)
        
       
        print(f"Se tardará aproximadamente {auto} {tiempo1} en auto; y {moto} {tiempo2} en moto")

#Fin reto 4
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
                    elif opcion == 3:
                        MostrarRestaurantesFav(coordenada)         
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