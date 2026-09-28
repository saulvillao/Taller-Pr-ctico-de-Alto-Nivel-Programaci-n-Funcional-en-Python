# Nivel 1 - Ejercicio 2: Multiplicador Paramétrico con Mapeo
#
# Recibe una lambda de operación (suma, multiplicación, potencia, etc.) y un factor.
# El closure aplica esa lambda usando el factor que quedó encapsulado en su entorno léxico.

def crear_operador(factor, operacion_lambda):
    def operador(valor):
        return operacion_lambda(valor, factor)
    return operador


if __name__ == "__main__":
    operador_doble = crear_operador(2, lambda v, f: v * f)
    print(operador_doble(15))  # 30
