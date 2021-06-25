cantidad=1
totalnomina=0
nEmpleados=int(input("Por favor ingrese el número de empleados:"))
while cantidad<=nEmpleados:
    salario=int(input("Por favor ingrese el salario del empleado "+cantidad+": "))
    if salario<1000:
        salario=salario*1.12
    if salario>=1000 and salario<=2500:
        salario=salario*1.10
    if salario>2500:
        salario=salario*1.08
    print("El nuevo sueldo es: ",salario)
    totalnomina=totalnomina+salario
    cantidad=cantidad+1
print ("La nomina total de empleados es: ",totalnomina)