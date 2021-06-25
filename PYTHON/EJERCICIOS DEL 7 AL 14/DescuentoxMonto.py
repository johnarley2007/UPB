print ("Bienvenido al programa, que calcula el descuento según el monto ingresado")
print ("********************************************************************")


import os
"""var = os.name
print ("el sistema operativo de mi computador es"+var)

os.system ("clear")"""
def borrarPantalla ():
    if  os.name == "posix":
        os.system ("clear")
    elif os.name== "ce" or os.name== "nt" or os.name== "dos":
        os.system ("cls")
borrarPantalla()

totalmonto=0
monto=int(input ("Por favor escriba el monto: "))
if monto>0:
    if monto>100:
       descuento=monto-(monto*0.1)
       porcentaje=("10%")
    else: 
       descuento=monto-(monto*0.02)
       porcentaje=("2%")
    print("El monto ingresado es: ",monto)
    print("El porcentaje del descuento final es: ",porcentaje," y el descuento total sera:",descuento)
else:
    exit ("Usted ingresó un valor negativo")


