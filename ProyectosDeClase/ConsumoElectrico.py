# Nombre: Gerald Alexander Penaranda Pereira
# Problema seleccionado: Problema 6. Consumo energético durante una ola de calor



cantidad_equipos = int(input("Ingresar cantidad de equipos: "))
potencia_watts = float(input("Ingresar potencia de cada  equipo en watts: "))
horas_por_dia = int(input("Ingresar horas de funcionamiento por dia: "))

if horas_por_dia < 0 or horas_por_dia > 24:
   print("Error de dato: Las horas no son correctas.")
   
else:
   cantidad_dias =int(input("Ingresar cantidad de dias de funcionamiento: "))
   precio_por_kwh = float(input("Ingresar precio actual del kilowatt: "))

   consumo_total_kwh = cantidad_equipos * potencia_watts * horas_por_dia * cantidad_dias / 1000

   calcular_costo_total = consumo_total_kwh * precio_por_kwh

   print("Consumo energético total (kWh):",consumo_total_kwh)
   print("Costo total estimado: ₡ ",calcular_costo_total)