from os import system
import os
system("clear")

x = 51661
y = 16615
listacoordenadas=[]
listadepuracion=[[10.103,-74.902],
                 [10.115,-75.085],
                 [10.108,-74.801]]

def IngresarCoordenadas(listaoriginal):
    listaduplicada=list(listaoriginal)
    for x in range (0,3):
        listaduplicada.append([])
        lat=input("Ingrese la latitud: ")
        while lat == "" or lat == " ":
            lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lat=float(lat)
        if lat >= 5.413 and lat <= 5.119:
            lon=input("Ingrese la longitud: ")
            while lon == "" or lon == " ":
                lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
            lon=float(lon)
            if lon >= -76.132 and lon <= -76.619:
                listaduplicada[x].insert(0,lat)
                listaduplicada[x].insert(1,lon)
                
                
            else:
                listaduplicada=[]
                return listaduplicada
        else:
            listaduplicada=[]
            return listaduplicada
    print("Coordenadas Ingresadas correctamente")
    time.sleep(2)    
    return listaduplicada

#Creamos la función ordenar latitudes (primero se ejecuta imprimir coordenadas)
def Ordenarlatitudes(listaoriginal):
    #Creamos una función anónima que nos retorna el valor mínimo; ubicado en la posición 0 de la lista original
    #Es decir pasamos por todas las latitudes y buscamos el menor
    print(f"La coordenada que está mas al sur es: {min(listaoriginal, key=lambda posicion: posicion[0])}")

#Creamos la función ordenar longitudes (primero se ejecuta imprimir coordenadas)
    #Creamos una función anónima que nos retorna el valor máximo; ubicado en la posición 1 de la lista original
    #Es decir pasamos por todas las longitudes y buscamos el mayor
def OrdenarLongitudes(listaoriginal):
    print(f"La coordenada que está mas al oriente es: {max(listaoriginal, key=lambda posicion: posicion[1])}")
    
#Imprimimos la suma de todos los elementos de cada sublista en la posición 0 (latitudes)
#y dividimos entre 3
def PromedioCoordenadas(listaoriginal):
    print(f"EL promedio de las latitudes es: {(listaoriginal[0][0]+listaoriginal[1][0]+listaoriginal[2][0])/3}")

#Creamos la función que imprime las coordenadas
def ImprimirCoordenads(listaoriginal):
    
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")
    #creamos un for que pasará imprimiendo la sublista X ambas posiciones
    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{listaduplicada[x][0]}' Longitud: '{listaduplicada[x][1]}'")
    #llamamos las funciones de ordenar y promedio y mandamos la lista completa como parámetros
    Ordenarlatitudes(listaduplicada)
    OrdenarLongitudes(listaduplicada)
    PromedioCoordenadas(listaduplicada)
    #guardamos la coordenada que el usuario moverá en una variable llamada choice
    choice=int(input("Por favor ingrese la opción que desea modificar:"))
    #revisamos si choice es un valor válido
    if choice !=1 and choice !=2 and choice !=3:
        ErrorConMensaje("Esa opción es inválida")
        return #En caso de error hacemos un return
    else:
        #Si son datos válidos llamamos actualizar coordenadas
        #Mandamos como parámetros choice y la lista
        ActualizarCoordenadas(choice,listaoriginal)
        

def ActualizarCoordenadas(choice,listaoriginal):
    #Duplicamos la lista para ganar acceso a sus métodos
    listaduplicada=list(listaoriginal)
    choice=choice-1 #Le restamos uno a choice para arreglar el desfaze visual del menú
     #Pedimos por la latitud y longitud usando la misma logica de la función ingresar coordenadas
    lat=input("Ingrese la latitud: ")
    while lat == "" or lat == " ":
        lat=input("La latitud no puede estar en blanco, por favor ingrésela de nuevo:")
    lat=float(lat)
    if lat >= 5.413 and lat <= 5.119:
        lon=input("Ingrese la longitud: ")
        while lon == "" or lon == " ":
            lon=input("La longitud no puede estar en blanco, por favor ingrésela de nuevo:")
        lon=float(lon)
        if lon >= -76.132 and lon <= -76.619:
            #Reemplazamos los valores 0 y 1 de la sublista choice, por latitud y longitud
            listaduplicada[choice][0]=lat
            listaduplicada[choice][1]=lon
            
        else:
            ErrorConMensaje("Longitud fuera del rango")
            listaduplicada=[listaoriginal] #En caso de error retornamos la lista original (sin cambios)
            return listaduplicada
    else:
        ErrorConMensaje("Latitud fuera del rango")
        listaduplicada=[listaoriginal] 
        return listaduplicada
    
    return listaduplicada #En caso éxito retornamos la nueva lista


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
                        if listacoordenadas==[]:
                            listacoordenadas=IngresarCoordenadas(listacoordenadas)
                        else:
                            #Llamamos la función imprimir coordenadas
                            ImprimirCoordenads(listacoordenadas)
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