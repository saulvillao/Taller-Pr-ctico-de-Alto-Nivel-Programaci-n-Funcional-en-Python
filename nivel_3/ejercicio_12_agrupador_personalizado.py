# Nivel 3 - Ejercicio 12: Reductor / Agrupador Personalizado
#
# Reduce una lista de diccionarios en un diccionario de grupos. La lambda fn_clave decide
# cuál es la clave de agrupación para cada elemento.

def agrupar_por(lista, fn_clave):
    resultado = {}
    for elemento in lista:
        clave = fn_clave(elemento)
        resultado.setdefault(clave, []).append(elemento)
    return resultado


if __name__ == "__main__":
    personas = [
        {"nombre": "Ana", "ciudad": "Quito"},
        {"nombre": "Luis", "ciudad": "Guayaquil"},
        {"nombre": "Marco", "ciudad": "Quito"},
    ]
    print(agrupar_por(personas, lambda p: p["ciudad"]))
