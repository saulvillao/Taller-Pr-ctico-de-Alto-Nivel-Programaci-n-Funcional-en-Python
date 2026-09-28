# Nivel 3 - Ejercicio 13: Ejecutor Repetitivo con Estado Accesible
#
# Ejecuta fn_tarea N veces y guarda cada resultado en una lista privada (historial).
# Retorna un closure 'accesor' de solo lectura que expone ese historial sin permitir
# modificarlo directamente.

def ejecutar_y_rastrear(fn_tarea, n):
    historial = [fn_tarea() for _ in range(n)]
    def obtener_historial():
        return historial
    return obtener_historial


if __name__ == "__main__":
    contador_dados = [0]

    def lanzar_dado():
        contador_dados[0] += 1
        return (contador_dados[0] * 7) % 6 + 1  # determinístico para reproducibilidad

    historial = ejecutar_y_rastrear(lanzar_dado, 5)
    print(historial())
