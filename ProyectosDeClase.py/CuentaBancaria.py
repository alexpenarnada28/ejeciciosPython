

saldo_bancario_disponible  = 250000
continuar = True
retiros_exitosos = 0

# Continúa con la ejecución del programa utilizando los datos ingresados por el usuario.
while continuar:


    monto_retiro_bancario = float(input("Ingrese el monto que desea realizar: "))
    
    if (monto_retiro_bancario >= 5000) and (monto_retiro_bancario <= 100000):
        if(monto_retiro_bancario <= saldo_bancario_disponible):
            # El monto del retiro está entre 5000 y 100000; se comprueba que el saldo de la cuenta sea suficiente. 
            repuesta = input(f"¿Desea continuar con el retiro de {monto_retiro_bancario}? (sí/no):")
            if repuesta.lower() == "si":
                saldo_total_disponible = saldo_bancario_disponible - monto_retiro_bancario 
                retiros_exitosos = retiros_exitosos + 1
                print("Retiro exitoso.")
                print(f"El saldo de su cuenta actualmente es de: {saldo_total_disponible}")
            else:
                print("Retiro cancelado. ")
        else:
            print("No cuenta con el dinero suficiente para el retiro.")
    else:
        print("Monto de retiro invalido, ingrese un monto de entre 5,000 y 100,000. ")

     
     # Bloque que me permite cerrar el ciclo.
    repuesta = input("Desea realizar otra transacion? (si/no):")
    if repuesta.lower() == "no":
        continuar = False

print("El monto disponible en su cuenta es: ", saldo_total_disponible)
print("Retiros exitosos ",retiros_exitosos)
print("Gracias por el retiro. ")










    
        
        