"""
Tipos de datos:
    - números enteros: int
    - números decimales: float
    - string: str
"""

# Conocer el tipo de dato
print("Tipo de dato:", type("6"))

datoInput = input("Ingrese un dato: ")
print("Tipo de dato:", type(datoInput))


numeroEntero = int(input("Ingrese un número entero: "))
print("Tipo de dato:", type(numeroEntero))
print("Número entero:", numeroEntero)
print("-" * 50)

numeroDecimal = float(input("Ingrese un número decimal: "))
print("Tipo de dato:", type(numeroDecimal))
print("Número decimal:", numeroDecimal)

resultado =  numeroDecimal * numeroEntero
print(numeroDecimal, "*", numeroEntero, "=", resultado)

