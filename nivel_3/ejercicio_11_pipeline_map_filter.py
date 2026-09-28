# Nivel 3 - Ejercicio 11: Pipeline de Mapeo y Filtrado Combinado
#
# HOF pura (sin estado) que combina 'filter' y 'map' internamente, delegando la condición
# y la transformación a dos lambdas independientes.

def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))


if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(procesar_coleccion(numeros, lambda n: n % 2 == 0, lambda n: n ** 2))
    # [4, 16, 36, 64, 100]
