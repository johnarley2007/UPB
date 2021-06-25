print ("Bienvenido al programa, que calcula la nota final de programación")
print ("********************************************************************")
parcial1=float(input ("Por favor escriba la nota del primer parcial: "))#int se utiliza para décimal.
parcial2=float(input ("Por favor escriba la nota del segundo parcial "))
parcial3=float(input ("Por favor escriba la nota del tercer parcial "))
examen=float(input ("Por favor escriba la nota del exámen "))
trabajofinal=float(input ("Por favor escriba la nota del trabajo final "))
pparcial=(((parcial1+parcial2+parcial3)/3)*0.55)#Se suman las 3 notas parciales y se multiplica por el porcentaje asignado.
rexamen=(examen*0.3)#Se multiplica por el 30%.
rtrabajofinal=(trabajofinal*0.15)#Se multiplica por el 15%.
resultado=float(pparcial+rexamen+rtrabajofinal)#Se debe poner la variable como flotante para que nos arroje el resultado.
print ("La nota final del estudiante es: ",resultado)