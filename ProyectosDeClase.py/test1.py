"""
Acceso a una plataforma educativa: Una plataforma educativa permite acceder a un curso únicamente cuando se cumplen determinadas condiciones.

El programa debe solicitar:
    - Edad del estudiante.
    - Si está matriculado en el curso.
    - Si tiene la cuenta activa.
    - Si ha realizado el pago correspondiente.

Las reglas son:
    - El estudiante debe tener 18 años o más.
    - Debe estar matriculado en el curso.
    - Su cuenta debe estar activa.
    - Además, debe haber realizado el pago del curso.
    - Si todas las condiciones se cumplen, mostrar "Acceso permitido".
    - En cualquier otro caso, mostrar "Acceso denegado".
"Acceso restringido":
    - menor de edad y pagó 
    - 
    
"""
edad = int(input("Ingrese la edad: "))


if edad >= 18: 
    matriculado = input("¿Está matriculado? (si/no): ")
    cuenta_activa = input("¿La cuenta está activa? (si/no): ")
    pago = input("¿Ha realizado el pago? (si/no): ")
    if matriculado == "si" and cuenta_activa == "si" and pago == "si":
        print("Acceso permitido")
    else:
        print("Acceso denegado")
elif edad < 18 and edad > 0:
    print("Acceso restringido")
else:
    print("Edad no permitida")
edad = int(input("Ingrese la edad: "))
matriculado = input("¿Está matriculado? (si/no): ")
cuenta_activa = input("¿La cuenta está activa? (si/no): ")
pago = input("¿Ha realizado el pago? (si/no): ")

if edad >= 18 and matriculado == "si" and cuenta_activa == "si" and pago == "si":
    print("Acceso permitido")
else:
    print("Acceso denegado")
#######

"""
Descuento en una tienda: Una tienda desea determinar si un cliente puede recibir un descuento especial en su compra.

El programa debe solicitar:

Edad del cliente.
Monto total de la compra.
Si posee una tarjeta de cliente frecuente.
Las reglas son:

Recibe un 10 % de descuento si tiene tarjeta de cliente frecuente y la compra es de al menos ₡50 000.
También recibe un 10 % de descuento si tiene 65 años o más, independientemente del monto de la compra.
Si no cumple ninguna de las condiciones anteriores, no recibe descuento.
El programa debe mostrar el monto original, el porcentaje de descuento y el monto final.
"""
edad = int(input("Ingrese la edad: "))
compra = float(input("Ingrese el monto de la compra: "))
tarjeta = input("¿Tiene tarjeta de cliente frecuente? (si/no): ")

if (tarjeta == "si" and compra >= 50000) or edad >= 65:
    descuento = 10
else:
    descuento = 0

monto_descuento = compra * descuento / 100
monto_final = compra - monto_descuento

print("Monto original:", compra)
print("Porcentaje de descuento:", descuento, "%")
print("Monto final:", monto_final)


"""
Clasificación de una contraseña: Una aplicación necesita determinar si una contraseña cumple con ciertos requisitos básicos de seguridad.

El programa debe solicitar:

Longitud de la contraseña.
Si contiene al menos un número.
Si contiene al menos una letra mayúscula.
Si contiene al menos un carácter especial.
Las reglas son:

Una contraseña es segura si tiene al menos 8 caracteres, contiene un número, una mayúscula y un carácter especial.
Si tiene menos de 8 caracteres, debe clasificarse como insuficiente.
Si tiene 8 caracteres o más pero le falta alguno de los elementos de seguridad, debe clasificarse como moderada.
El programa debe mostrar la clasificación obtenida.
"""
longitud = int(input("Ingrese la longitud de la contraseña: "))
numero = input("¿Contiene al menos un número? (si/no): ")
mayuscula = input("¿Contiene una letra mayúscula? (si/no): ")
especial = input("¿Contiene un carácter especial? (si/no): ")

if longitud < 8:
    print("Contraseña insuficiente")
elif longitud >= 8 and numero == "si" and mayuscula == "si" and especial == "si":
    print("Contraseña segura")
else:
    print("Contraseña moderada")


"""
Permiso para conducir: Un sistema desea determinar si una persona puede conducir un vehículo de acuerdo con determinadas condiciones.

El programa debe solicitar:

Edad de la persona.
Si posee licencia de conducir.
Si la licencia está vigente.
Si tiene permiso especial.
Las reglas son:

Una persona puede conducir si tiene 18 años o más, posee licencia y esta se encuentra vigente.
Una persona menor de 18 años solamente puede continuar si posee un permiso especial, de acuerdo con las reglas establecidas por el ejercicio.
Si la licencia no está vigente y no posee permiso especial, no puede conducir.
El programa debe indicar si la persona puede o no conducir.
"""
edad = int(input("Ingrese la edad: "))
licencia = input("¿Posee licencia? (si/no): ")
vigente = input("¿La licencia está vigente? (si/no): ")
permiso = input("¿Tiene permiso especial? (si/no): ")

if edad >= 18 and licencia == "si" and vigente == "si":
    print("Puede conducir")
elif edad < 18 and permiso == "si":
    print("Puede conducir")
else:
    print("No puede conducir")