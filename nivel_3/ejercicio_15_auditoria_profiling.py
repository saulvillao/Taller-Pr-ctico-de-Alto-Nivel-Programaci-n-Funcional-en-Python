# Nivel 3 - Ejercicio 15: Decorador / HOF de Profiling y Auditoría
#
# Patrón decorador: envuelve una función objetivo, mide su tiempo de ejecución con
# time.perf_counter() y delega el reporte final a una lambda 'logger' inyectada por el
# usuario.

import time

def auditar_ejecucion(fn_objetivo, fn_logger):
    def ejecutar(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = fn_objetivo(*args, **kwargs)
        duracion = time.perf_counter() - inicio
        fn_logger({
            "funcion": fn_objetivo.__name__,
            "duracion_seg": round(duracion, 6),
            "resultado": resultado
        })
        return resultado
    return ejecutar


if __name__ == "__main__":
    reportes = []
    suma_auditada = auditar_ejecucion(lambda a, b: a + b, lambda info: reportes.append(info))
    resultado = suma_auditada(4, 6)
    print(resultado, reportes[-1])
