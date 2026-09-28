# Nivel 2 - Ejercicio 7: Acumulador con Filtro de Aceptación
#
# Mantiene un total privado (nonlocal). Solo suma un valor si la lambda-criterio lo aprueba
# primero, actuando como un filtro de aceptación antes de acumular.

def crear_acumulador_validado(criterio_lambda):
    total = 0
    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumular


if __name__ == "__main__":
    acumulador_pares = crear_acumulador_validado(lambda v: v % 2 == 0)
    print(acumulador_pares(3), acumulador_pares(4), acumulador_pares(10))  # 0 4 14
