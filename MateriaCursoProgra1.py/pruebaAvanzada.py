"""
Una tienda vende videojuegos en tres ediciones. El precio depende de la edición seleccionada.

Precios establecidos:

Edición estándar: ₡25 000.
Edición deluxe: ₡35 000.
Edición coleccionista: ₡50 000.

El programa debe solicitar:
    - Tipo de edición.
    - Cantidad de videojuegos.
    - Si el cliente es estudiante.

Utilice las siguientes reglas:
    - Si el cliente compra 3 videojuegos o más, recibe un 10 % de descuento.
    - Si además es estudiante, recibe un 5 % adicional sobre el precio después del primer descuento.
    - Si compra menos de 3 videojuegos, no recibe el descuento por cantidad.
"""
# Constantes
ESTANDAR = 25000
DELUXE = 35000
COLECCIONISTA = 50000

DESCUENTO_CANTIDAD = 0.10
DESCUENTO_ESTUDIANTE = 0.05

# Seleccionar precio
edicion = input("Ingrese la edición (1: estandar, 2: deluxe, 3: coleccionista): ")
if edicion == "1":
    precio = ESTANDAR
elif edicion == "2":
    precio = DELUXE
else:
    precio = COLECCIONISTA

cantidad = int(input("Ingrese la cantidad de videojuegos: "))

subtotal = precio * cantidad # Subtotal

# Primer descuento
if cantidad >= 3:
    descuento_cantidad = subtotal * DESCUENTO_CANTIDAD
else:
    descuento_cantidad = 0

precio_despues_cantidad = subtotal - descuento_cantidad

# Descuento de estudiante
estudiante = input("¿Es estudiante? (si/no): ")
if estudiante == "si":
    descuento_estudiante = precio_despues_cantidad * DESCUENTO_ESTUDIANTE
else:
    descuento_estudiante = 0

# Total
total = precio_despues_cantidad - descuento_estudiante
print("Total:", total)