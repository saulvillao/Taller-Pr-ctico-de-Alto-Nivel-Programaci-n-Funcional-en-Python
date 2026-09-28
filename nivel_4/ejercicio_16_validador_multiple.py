# Nivel 4 - Ejercicio 16: Validador Compuesto de Reglas de Negocio
#
# Usa *args para recibir un número variable de lambdas-regla. El closure exige que TODAS
# se cumplan (función all()), útil para validar objetos contra varias reglas de negocio
# a la vez.

def crear_validador_multiple(*lambdas_criterios):
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar


if __name__ == "__main__":
    validador_producto = crear_validador_multiple(
        lambda p: p["precio"] > 0,
        lambda p: p["stock"] >= 0,
        lambda p: len(p["nombre"]) > 2
    )
    print(validador_producto({"nombre": "Mouse", "precio": 15, "stock": 3}))
    print(validador_producto({"nombre": "X", "precio": -5, "stock": 3}))
