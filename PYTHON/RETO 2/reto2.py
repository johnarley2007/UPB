from os import system
system("clear")
print ("Bienvenido al sistema de ubicación para zonas públicas WIFI")
x="51661"
y="16615"
try:
    usuario=(input("Digite el ususario: "))
    if usuario==x:
        system("clear")
        password=(input("Digite la contraseña: "))
        if password==y:
            system("clear")
            print("Bienvenido")
            termino1=661
            termino2=(2*1)+5-1
            captcha=str(print(termino1," + ",termino2,"="))
            validar=input()
            if validar=="667":
                system("clear")
                print("Sesión iniciada")
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
                        elif opcion == 7:
                            print("Hasta pronto")
                    except ValueError:
                        print("Error")
                        contador +=1
                else:
                    system("clear")
                    print("Error")
            else:
                system("clear")
                print("Error")
        else:
            system("clear")
            print("Error")
except:
        system("clear")
        print("Error")