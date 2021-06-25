print ("Bienvenido al programa, que calcula el salario de un trabajador por horas laboradas y extras")
print ("********************************************************************")
nombreEmpleado=str(input("Digite el nombre del empleado: "))
totalHoras=float(input ("Por favor escriba la cantidad de horas trabajadas en el mes: "))#float se utiliza para décimal.
valorHora=int(input ("Por favor escriba el valor de la hora: "))#int se utiliza para entero.
valorHoraExtra=float(valorHora*0.5+valorHora)
if totalHoras>=40:
    salario=float(40*valorHora)+((totalHoras-40)*valorHoraExtra)
else:
    salario=float(totalHoras*valorHora)
print ("El salario final de",nombreEmpleado,"es: $",salario)