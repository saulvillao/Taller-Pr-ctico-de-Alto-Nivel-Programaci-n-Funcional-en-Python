# Nivel 2 - Ejercicio 8: Promediador con Eliminación de Valores Extremos
#
# Guarda todos los datos recibidos en una lista privada y, en cada llamada, recalcula el
# promedio excluyendo los valores atípicos según la lambda de filtro de ruido.

def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []
    def agregar(valor):
        datos.append(valor)
        validos = [v for v in datos if filtro_ruido_lambda(v)]
        if not validos:
            return 0
        return round(sum(validos) / len(validos), 2)
    return agregar


if __name__ == "__main__":
    promediador = crear_promediador_filtrado(lambda v: 0 <= v <= 100)
    print(promediador(10), promediador(90), promediador(9999))  # 10.0 50.0 50.0
