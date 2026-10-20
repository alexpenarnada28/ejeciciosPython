# --------------------------------------------------------------- Datos de entrada 
hasValidTicket = input("¿Tiene una entrada válida? (si/no): ")
age = int(input("Ingrese su edad: "))
belongsToInstitution = input("¿Pertenece a la Univercidad CENFOTEC? (si/no): ")
entryHour = int(input("Ingrese la hora de ingreso (0-23): "))

# --------------------------------------------------------------- Condiciones / deciciones 
if hasValidTicket == "no" or age < 18:
    print("Acceso denegado")
elif belongsToInstitution == "si" and entryHour < 18:
    print("Acceso permitido: acceso preferencial")
else:
    print("Acceso permitido: acceso general")


    # --------------------------------------------------------------- Datos de entrada 
hasValidTicket = input("¿Tiene una entrada válida? (si/no): ")
age = int(input("Ingrese su edad: "))

# --------------------------------------------------------------- Condiciones / deciciones 
if hasValidTicket == "no" or age < 18:
    print("Acceso denegado")
else: 
    belongsToInstitution = input("¿Pertenece a la Univercidad CENFOTEC? (si/no): ")
    entryHour = int(input("Ingrese la hora de ingreso (0-23): "))
    if belongsToInstitution == "si" and entryHour < 18:
        print("Acceso permitido: acceso preferencial")
    else:
        print("Acceso permitido: acceso general")