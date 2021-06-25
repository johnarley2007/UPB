menu = ["Cambiar contraseña", "Ingresar coordenadas actuales", "Ubicar zona wifi más cercana", "Guardar archivo con ubicación cercana", "Actualizar registros de zonas wifi desde archivo", "Elegir opción de menú favorita", "Cerrar sesión."]
contador = 0
while True:
                    if contador >= 3:
                        print ("Error1")
                        exit()
                    for i in range(7):
                        print(str(i+1)+". ", menu[i])
                    try:
                        opcion = int(input("Elija una opción"))
                        if opcion < 1 or opcion > 7:
                            print("Error2")
                            contador +=1
                            time.sleep=(2)
                        elif opcion==6:
                            try:
                                favorita = int(input("Seleccione opción favorita"))
                                contador = 0
                                if favorita < 1 or favorita > 5:
                                    print("Error3")
                                    exit()
                                else:
                                    try:
                                        primer_digito = int(input("Número antes del siete: "))
                                        if primer_digito == 6:
                                            segundo_digito = int(input("Número que representa la unidad:"))
                                            if primer_digito == 1:
                                                favorita -=1
                                                temporal = menu[favorita]
                                                menu.pop(favorita)
                                                menu.insert(0,temporal)
                                            else:
                                                print("Error4")
                                        else:
                                            print("Error5")
                                    except ValueError:
                                        print("Error6")
                            except ValueError:
                                print("Error7")
                                exit()
                        elif opcion >=1 and opcion <=5:
                                print ("Usted ha elegido la opción "+str(opcion)+"")
                                exit()
                        elif opcion == 7:
                            print("Hasta pronto")
                    except ValueError:
                        print("Error8")
                        contador +=1