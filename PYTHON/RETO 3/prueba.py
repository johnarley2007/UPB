from os import system
import os
import time                
menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión."]
contador = 0
while True:
                    if contador >= 3:
                        print ("Error")
                        exit()
                    for i in range(7):
                        print(str(i+1)+". ", menu[i])
                    try:
                        opcion = int(input("Elija una opción"))
                        if opcion < 1 or opcion > 7:
                            print("Error")
                            contador +=1
                            time.sleep=(2)
                        elif opcion==6:
                            try:
                                favorita = int(input("Seleccione opción favorita"))
                                contador = 0
                                if favorita < 1 or favorita > 5:
                                    print("Error")
                                    exit()
                                else:
                                    try:
                                        primer_digito = int(input("Número antes del siete: "))
                                        if primer_digito == 6:
                                            segundo_digito = int(input("Número que representa la unidad:"))
                                            if segundo_digito == 1:
                                                favorita -=1
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
                    #Inicio del reto 3
                        if menu [opcion - 1] == "Cambiar contraseña":
                                contrasena_2 = (input("Digite la clave actual: "))
                                if password == contrasena_2:
                                    contrasena_2 = (input("Digite la nueva clave: "))
                                    if password != contrasena_2:
                                        password = contrasena_2
                                    else:
                                        print("La contraseña actual no puede ser igual a la anterior")

                                else:
                                    print("Error")
                                    exit ()
                        elif menu [opcion - 1] == "Ingresar las coordenadas actuales":
                            if len(coordenadas) == 0:
                                coordenadas =[[0]*2 for i in range(3)]
                                for i in range(3):
                                    for j in range(2):
                                        try:
                                            if j == 0:
                                                coordenadas[i][j] = float(input("Digite la latitud para la coordenada "+str(i+1) +": "))
                                                coordenadas[i][j] = round(coordenadas[i][j],3)
                                                if coordenadas[i][j] > 5.413 or coordenadas[i][j] < 5.119:
                                                    print("Error coordenada")
                                                    exit()
                                                else:
                                                    coordenadas[i][j] = float(input("Digite la longitud para la coordenada "+str(i+1) +": "))
                                                    coordenadas[i][j] = round(coordenadas[i][j],3)
                                                    if coordenadas[i][j] > -76.132 or coordenadas[i][j] < -76.619:
                                                        print("Error coordenada")
                                                        exit()
                                        except ValueError():
                                            print("Error")
                                            exit()
                                else:
                                    for i in range(3):
                                        print("coordenada [latitud,longitud] "+str(i+1)+" :", coordenadas[i])
                                    print("la coordenada "+str(coordenadas.index(max(coordenadas))+"es la que está más al norte "))
                                    latitud_promedio=0
                                    longitud_promedio=0
                                    for i in range(3):
                                        for j in range(2):
                                            if j==0:
                                                latitud_promedio = latitud_promedio + coordenadas[i][j]
                                            else:
                                                longitud_promedio = longitud_promedio + coordenadas[i][j]
                                    latitud_promedio /=3
                                    longitud_promedio /=3
                                    latitud_promedio = round(latitud_promedio,3)
                                    longitud_promedio = round(longitud_promedio,3)
                                    print("la coordenada promedio de todos los puntos [latitud,longitud] : [" + str (latitud_promedio)+ "," + str (longitud_promedio)+ "]")
                                    try:
                                        actualizar_coordenada = int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada. Presione 0 para regresar al menú"))
                                        if actualizar_coordenada >= 1 and actualizar_coordenada <= 3:
                                            coordenadas[actualizar_coordenada - 1 [0]] = round(float(input("Digite la latitud para la coordenada "+ str(actualizar_coordenada))),3)
                                            if coordenadas [i][j] > 5.413 or coordenadas[i][j] < 5.119:
                                                print("Error coordenada")
                                                exit()
                                            
                                            coordenadas[actualizar_coordenada - 1 [1]] = round(float(input("Digite la longitud para la coordenada "+ str(actualizar_coordenada))),3)
                                            if coordenadas [i][j] > -76.132 or coordenadas[i][j] < -76.619:
                                                print("Error coordenada")
                                                exit()
                                        elif actualizar_coordenada ==0:
                                            pass
                                        else:
                                            print("Error actualización")
                                            exit()
                                    except ValueError():
                                        print("Error actualización")
                                        exit()    
                        elif opcion == 7:
                            print("Hasta pronto")
                    except ValueError:
                        print("Error")
                        contador +=1
else:
                    system("clear")
                    print("Error")