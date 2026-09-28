# Nivel 2 - Ejercicio 9: Limitador de Tasa Inteligente (Rate Limiter con Reset)
#
# Cuenta ejecuciones en una variable privada (nonlocal). Al superar max_intentos, no solo
# bloquea la ejecución sino que además dispara una lambda de alerta (callback) inyectada
# por el usuario.

def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def ejecutar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return False
        return True
    return ejecutar


if __name__ == "__main__":
    alertas = []
    limitador = crear_limitador_avanzado(2, lambda i: alertas.append(f"Límite excedido en intento {i}"))
    print(limitador(), limitador(), limitador(), alertas)
