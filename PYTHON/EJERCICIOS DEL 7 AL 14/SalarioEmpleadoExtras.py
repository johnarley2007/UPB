print ("Bienvenido al programa, que calcula el salario de un trabajador por horas laboradas con su respectivo incremento")
print ("********************************************************************")
valorHorasExtras=0
nombreEmpleado=str(input("Digite el nombre del empleado: "))
totalHoras=float(input ("Por favor escriba la cantidad de horas trabajadas en el mes: "))#float se utiliza para décimal.
valorHora=int(input ("Por favor escriba el valor de la hora: "))#int se utiliza para entero.
if totalHoras>40:
    horasExtras=totalHoras-40
    valorHorasExtras=(horasExtras*valorHora)*1.5
    horastrabajo=totalHoras-horasExtras
    salarioextra=horastrabajo*valorHora+valorHorasExtras
    salariobasico=horastrabajo*valorHora
    print ("El salario de",nombreEmpleado,"es: $",salarioextra)
    print ("Las horas básicas son: ",horastrabajo,"que equivalen a ",salariobasico)
    print ("Las horas extras son: ",horasExtras,"que equivalen a ",valorHorasExtras)
else:
    salario=totalHoras*valorHora
    print ("El salario de",nombreEmpleado,"es: $",salario)