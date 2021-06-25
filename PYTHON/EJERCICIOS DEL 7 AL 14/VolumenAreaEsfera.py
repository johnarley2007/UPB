print ("Bienvenido al programa, que calcula el volúmen y el área de una esfera")
print ("********************************************************************")
import math
radio=float(input("Digite el radio de la esfera: "))
area=float((4*3.1416)*(radio**2))
volumen=float(((4/3)*3.1416)*(radio**3))
print ("El área de la esfera es:",area)
print ("El volumen de la esfera es:",volumen)