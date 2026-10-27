# nombre_variable = "dato que almacena la variable" # 10, 10.1, "A", "Ana", True, False

# nombre_lista = ["dato 1", "dato 2", "", "dato N"]

provincias = ["Puntarenas", "cARTAgo", "Heredia", 156846]
print("Lista de provincias:", provincias)

# Agregar datos al final 
provincias.append("San José")
print("Lista de provincias actualizada:", provincias)

# Eliminar el último elemento de la lista
provincias.pop()
print("Lista de provincias actualizada:", provincias)

"""
[
"Puntarenas",   índice  0    |       índice   -4
"Cartago",      índice  1    |       índice   -3
"Heredia",      índice  2    |       índice   -2
156846          índice  3    |       índice   -1
] 
"""

# Actualizar el dato de una posición en particular
provincias[3] = "San José"
print("Lista de provincias actualizada:", provincias)

provincias[-3] = "Cartago"
print("Lista de provincias actualizada:", provincias)

# Agregar datos en un índice particular
provincias.insert(2, "Limón")
print("Lista de provincias actualizada:", provincias)


# Consultar datos ['Puntarenas', 'Cartago', 'Limón', 'Heredia', 'San José']
print("Elemento en el índice -5:", provincias[-5])
print("Elemento en el índice 3:", provincias[3])


numeros_pares = {20, 40, 60, 80, 100}
colores = {"rojo", "blanco", "amarillo", "azul", "verde"}

# Ejercicio crear una lista de números, lista de números pares, lista de cosas, lista de números impares
jugadores = [1, 2, 3, 4, 5]
cosas = ["casa", "carro", "avión", "televisión"]
impares = [1, 3, 5, 7, 9]
utiles = ["cuaderno", "borrador", "tajador"]
          
print("Listas unidas:", jugadores + cosas)
print("Operación * en la lista:", 3 * utiles)
print("Operación * en la impares:", 3 * impares)

# Cantidad de elementos
colores = ["rojo", "blanco", "amarillo", "azul", "verde"]
print("Cantidad de elementos en la lista colores:", len(colores))

materias_favoritas = ["Química", "Matemática", "Física Matemática", "Estudios Sociales"]
materias_favoritas.sort()
print("Lista materias_favoritas ordenada:", materias_favoritas)

numeros = [3, 8, 15, 20, 7]
numeros.reverse()
print("Lista invertida:", numeros)


"""
Resumen de operaciones
Operación	                    Función o método	            Ejemplo
Agregar al final	            append()	                    clientes.append("Ana")
Insertar	                    insert()	                    clientes.insert(1, "Luis")
Eliminar por valor	            remove()	                    clientes.remove("Ana")
Eliminar por posición	        pop()	                        clientes.pop(0)
Eliminar con índice	            del	                            del clientes[2]
Contar elementos	            len()	                        len(clientes)
Buscar elemento	                in	                            "Ana" in clientes
Obtener índice	                index()	                        clientes.index("Ana")
Contar repeticiones	            count()	                        clientes.count("Ana")
Ordenar	                        sort()	                        clientes.sort()
Invertir	                    reverse()	                    clientes.reverse()
Copiar	                        copy()	                        clientes.copy()
Unir listas	                    +	                            lista1 + lista2
Repetir lista	                *	                            ["BAC"] * 3
Obtener sublista	            [:]	                            clientes[1:4]
Suma todos los elementos	   sum(lista)                       sum(saldos)
Devuelve el valor mayor	       max(lista)                       max(saldos)
Devuelve el valor menor	       min(lista)                       min(saldos)
Cuenta los elementos	       len(lista)                       len(saldos)
Calcula el promedio	           sum(lista)/len(lista)            sum(saldos)/len(saldos)
"""
