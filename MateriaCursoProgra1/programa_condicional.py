'''
Una institución organiza un evento presencial y necesita un sistema que determine si una persona puede ingresar y, en caso afirmativo, qué tipo de acceso recibirá.

Para tomar la decisión, el sistema debe conocer los siguientes datos:
    - La edad de la persona (age).
    - Si posee una entrada válida (hasValidTicket).
    - Si pertenece a la institución (belongsToInstitution).
    - La hora en la que intenta ingresar (entryHour).

La organización ha establecido las siguientes reglas:
    - Para ingresar, la persona debe tener una entrada válida.
    - Si no tiene una entrada válida, el acceso es denegado, independientemente de las demás condiciones.
    - Las personas menores de 18 años no pueden ingresar al evento.
    - Las personas de 18 años o más pueden continuar con la evaluación de las demás condiciones.
    - Si la persona pertenece a la institución y llega antes de las 18:00, recibe acceso preferencial.
    - Si pertenece a la institución pero llega a las 18:00 o después, recibe acceso general.
    - Si no pertenece a la institución, puede ingresar únicamente con acceso general.
'''


hasValidTicket = input("¿Tiene una entrada válida? (si/no): ")
age = int(input("Ingrese su edad: "))
belongsToInstitution = input("¿Pertenece a la Univercidad CENFOTEC? (si/no): ")
entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

# Posible solución 1
if hasValidTicket == "no":
    print("Acceso denegado: no tiene una entrada válida")
elif age < 18:
    print("Acceso denegado: es menor de edad")
elif belongsToInstitution == "si":
    if entryHour < 18: 
        print("Acceso permitido: acceso preferencial")
    else:
        print("Acceso permitido: acceso general")
else: 
    print("Acceso permitido: acceso general")

"""
# Posible solución 2
if hasValidTicket == "si":
    if age < 18:
        print("Acceso denegado: es menor de edad")
    elif belongsToInstitution == "si":
        if entryHour < 18: 
            print("Acceso permitido: acceso preferencial")
        else:
            print("Acceso permitido: acceso general")
    else: 
        print("Acceso permitido: acceso general")
else: 
    print("Acceso denegado: no tiene una entrada válida") """


# Posible solución 3
""" hasValidTicket = input("¿Tiene una entrada válida? (si/no): ")
if hasValidTicket == "no":
    print("Acceso denegado: no tiene una entrada válida")
else:
    age = int(input("Ingrese su edad: "))
    if age < 18:
        print("Acceso denegado: es menor de edad")
    else:
        belongsToInstitution = input("¿Pertenece a la Universidad CENFOTEC? (si/no): ")

        if belongsToInstitution == "si":
            entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

            if entryHour < 18:
                print("Acceso permitido: acceso preferencial")
            else:
                print("Acceso permitido: acceso general")
        else:
            print("Acceso permitido: acceso general") """

# Posible solución 4
# "texto".lower() Permite convertir un texto a letras minúsculas. Ejemplo: "Si", "sI", "SI", "si" serían convertidas a "si"
# "texto".upper() Permite convertir un texto a mayúsculas 

hasValidTicket = input("¿Tiene una entrada válida? (si/no): ").lower()

# "no"
if hasValidTicket == "no" :
    print("Acceso denegado: no tiene una entrada válida")
else:
    age = int(input("Ingrese su edad: "))

    if age < 18:
        print("Acceso denegado: es menor de edad")
    else:
        belongsToInstitution = input("¿Pertenece a la Universidad CENFOTEC? (si/no): ").upper()

        if belongsToInstitution == "SI":
            entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

            if entryHour < 18:
                print("Acceso permitido: acceso preferencial")
            else:
                print("Acceso permitido: acceso general")
        else:
            print("Acceso permitido: acceso general")


            
############################
            

age = 18

'''
Condicional simple
if condición: 
    código a ejecutar SI se cumple la condición 

if age > 18:  # 12 > 18: False
    print("Es mayor de edad") 
'''

'''
Condicional doble
if condición: 
    código a ejecutar SI se cumple la condición 
else: 
    código a ejecutar si NO se cumple la condición
'''

if age >= 18:  # 18 >= 18: True
    print("Es mayor de edad") 
else:
    print("Es menor de edad")

    '''
Condicional múltiple
if condición: 
    código a ejecutar SI se cumple la condición 
elif condición: 
    código a ejecutar SI se cumple la condición
else: 
    código a ejecutar si NO se cumplen las condicionales previas
'''

age = 8

if age < 1:                     # 8 < 1 : False
    print("Es un bebé")
elif age < 12:                  # 8 < 12 : True 
    print("Es un infante")
elif age < 18:                  
    print("Es adolescente")
else:
    print("Es mayor de edad")

    '''
Ejercicio: Modifique el programa anterior para: 
    - edad < 65 muestre es un adulto
    - edad mayor o igual a 65 muestre es un adulto mayor 
    - edad un número negativo muestre Error: debe ser un número positivo 
'''

ge = 8

if age < 65:                     # 8 < 1 : False
    print("Es un adulto")
elif age >= 65:                  # 8 < 12 : True 
    print("Es un adulto mayor")
elif age < 0:                  
    print( "Es adolescente")

'''
Condicional simple
if condición: 
    código a ejecutar SI se cumple la condición 

if age > 18:  # 12 > 18: False
    print("Es mayor de edad") 
'''

'''
Condicional doble
if condición: 
    código a ejecutar SI se cumple la condición 
else: 
    código a ejecutar si NO se cumple la condición


if age >= 18:  # 18 >= 18: True
    print("Es mayor de edad") 
else:
    print("Es menor de edad")
'''

'''
Condicional múltiple
if condición: 
    código a ejecutar SI se cumple la condición 
elif condición: 
    código a ejecutar SI se cumple la condición
else: 
    código a ejecutar si NO se cumplen las condicionales previas
'''

age = 79


if age < 0:                     
    print("Error: La edad debe ser un número positivo")
elif age == 0:
    print("Es un bebé")
elif age < 12:                  
    print("Es un infante")
elif age < 18:                  
    print("Es adolescente")
elif age < 65:                  
    print("Es adulto")
else:                  
    print("Es adulto mayor")


'''
Ejercicio: Modifique el programa anterior para: 
    - edad < 65 muestre es un adulto
    - edad mayor o igual a 65 muestre es un adulto mayor 
    - edad un número negativo muestre Error: La edad debe ser un número positivo 
'''


if hasValidTicket == "no" or age < 18:
    print("Acceso denegado")
elif belongsToInstitution == "si" and entryHour < 18:
    print("Acceso permitido: acceso preferencial")
else:
    print("Acceso permitido: acceso general")