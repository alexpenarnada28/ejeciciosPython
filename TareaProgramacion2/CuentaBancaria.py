#====================================================================================
# Nombre del estudiante: Gerald Alexander Peñaranda Pereira 
# Contexto seleccionado: Problema 1. Cajero automático
# Descripción: El programa simula un cajero automático para realizar retiros de dinero y 
# consultar el saldo disponible.
#====================================================================================

# Constantes.

MONTO_MINIMO = 5000
MONTO_MAXIMO = 100000
SALDO_INICIAL = 250000

# Inicialización del programa.

saldo_bancario_disponible  = SALDO_INICIAL
retiros_exitosos = 0
continuar = input("¿Desea realizar una transacción? (si/no): ").lower() == "si"

# Continúa con la ejecución del programa utilizando los datos ingresados por el usuario.

while continuar and saldo_bancario_disponible > 0:


    monto_retiro_bancario = float(input("Ingrese el monto que desea realizar: "))
    
    if (monto_retiro_bancario >= MONTO_MINIMO) and (monto_retiro_bancario <= MONTO_MAXIMO):
        if(monto_retiro_bancario <= saldo_bancario_disponible):

            # El monto del retiro está entre MONTO_MINIMO y MONTO_MAXIMO; se comprueba que el saldo de la cuenta sea suficiente. 
            
            repuesta = input(f"¿Desea continuar con el retiro de {monto_retiro_bancario}? (sí/no):")
            if repuesta.lower() == "si":
                saldo_bancario_disponible = saldo_bancario_disponible - monto_retiro_bancario 
                retiros_exitosos = retiros_exitosos + 1
                print("Retiro exitoso.")
                print(f"El saldo de su cuenta actualmente es de: {saldo_bancario_disponible}")
            else:
                print("Retiro cancelado. ")
        else:
            print("No cuenta con el dinero suficiente para el retiro.")
    else:
        print("Monto de retiro invalido, ingrese un monto de entre 5,000 y 100,000. ")

     
     # Bloque que me permite cerrar el ciclo.

    continuar = input("Desea realizar otra transacion? (si/no): ").lower() == "si"
   

# Salida final del programa.   

print("El monto disponible en su cuenta es: ", saldo_bancario_disponible)
print("Retiros exitosos ",retiros_exitosos)
print("Gracias por el retiro. ")










    
        
        