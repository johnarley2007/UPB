print ("Bienvenido al programa, que calcula el salario de un trabajador por horas laboradas con su respectivo incremento")
print ("********************************************************************")
nombreEmpleado=str(input("Digite el nombre del empleado: "))
totalHoras=float(input ("Por favor escriba la cantidad de horas trabajadas en el mes: "))#float se utiliza para décimal.
valorHora=int(input ("Por favor escriba el valor de la hora: "))#int se utiliza para entero.
salario=float(totalHoras*valorHora)
incremento=float(salario*0.10)
incSalario=float(incremento+salario)
print ("El salario de",nombreEmpleado,"es: $",salario)
print ("El incremento de",nombreEmpleado,"es: $",incremento)
print ("El salario final de",nombreEmpleado,"es: $",incSalario)