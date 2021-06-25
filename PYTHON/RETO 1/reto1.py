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