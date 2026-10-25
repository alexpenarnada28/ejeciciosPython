# Ingresamos los datos de entrada.
nombre_trabajador = input("Ingrese el nombre del trabajador: ")
horas_semanales = int(input("¿Cuántas horas trabajó esta semana? "))
pago_hora = float(input("Ingrese el salario por hora: "))

# Calculamos el ingreso semanal.
salario_devengado = horas_semanales * pago_hora

# Mostramos la salida del programa.
print("Trabajador:", nombre_trabajador)
print("Total de ingreso semanal:", salario_devengado)






