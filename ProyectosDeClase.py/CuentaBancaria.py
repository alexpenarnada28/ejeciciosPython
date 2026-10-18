# Constantes 

saldo_bancario_disponible  = 250000
retiros_existoso = 0

# Proceso en el cual el programa ejecuta las consiciones para proceder.

while True:
    saldo_bancario_disponible = 250000
    retiros_existoso = 0

    monto_retiro_bancario = float(input("Ingresar el monto que desea retirar: "))

    if monto_retiro_bancario >= 5000 and monto_retiro_bancario <= 100000 and monto_retiro_bancario <= saldo_bancario_disponible:
        print("Retiro valido")
        repuesta = input("Desea realizar otra trasferencia (si/no)")
    if repuesta == "no":
        print("Gracias por su retiro")
        break
    else:
        if monto_retiro_bancario >= 5000 or monto_retiro_bancario <=100000:
            print("Monto fuera del rango intenta otro monto")
        if monto_retiro_bancario <= saldo_bancario_disponible:
            print("Saldo insuficiente ")
        else:
            repuesta = input("Desea realizar otra trasferencia (si/no)")
        if repuesta == "no":
            print("Gracias por su retiro")
            break
