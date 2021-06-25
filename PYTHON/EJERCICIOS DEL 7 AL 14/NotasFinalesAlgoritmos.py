print ("Bienvenido al programa, que calcula la nota final de algoritmos")
print ("********************************************************************")
nombreEstudiante=str(input("Digite el nombre del estudiante: "))
corte1=float(input ("Por favor escriba la nota del primer corte: "))#int se utiliza para décimal.
corte2=float(input ("Por favor escriba la nota del segundo corte "))
parcial=float(input ("Por favor escriba la nota del tercer parcial final "))
resCorte1=(corte1*0.3)
resCorte2=(corte2*0.3)
rparcialfinal=(parcial*0.40)
resultado=float(resCorte1+resCorte2+rparcialfinal)#Se debe poner la variable como flotante para que nos arroje el resultado.
print ("La nota final del estudiante",nombreEstudiante,"es: ",resultado)