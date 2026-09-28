# Nivel 4 - Ejercicio 20: Mini-Query Engine sobre Listas de Objetos
#
# HOF de dos niveles (currying): primero fija el 'campo' a consultar y retorna otra función
# que recibe la lambda-condición; esta última retorna el filtro final que se aplica sobre
# la lista de diccionarios.

def crear_consultor(campo):
    def condicion(condicion_lambda):
        def filtrar(lista_objetos):
            return [obj for obj in lista_objetos if condicion_lambda(obj.get(campo))]
        return filtrar
    return condicion


if __name__ == "__main__":
    inventario = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 15},
        {"nombre": "Monitor", "precio": 300},
    ]
    consultar_precio = crear_consultor("precio")
    filtro_caros = consultar_precio(lambda precio: precio > 100)
    print(filtro_caros(inventario))
