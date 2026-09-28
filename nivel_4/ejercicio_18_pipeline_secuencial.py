# Nivel 4 - Ejercicio 18: Motor de Pipeline Secuencial (Currying / Middleware)
#
# Recibe *funciones_transformacion (lambdas) y retorna un closure que hace fluir un dato
# inicial secuencialmente por todas ellas, en el orden en que fueron pasadas (estilo
# middleware).

def crear_pipeline(*funciones_transformacion):
    def ejecutar_pipeline(dato_inicial):
        resultado = dato_inicial
        for funcion in funciones_transformacion:
            resultado = funcion(resultado)
        return resultado
    return ejecutar_pipeline


if __name__ == "__main__":
    limpiar_texto = crear_pipeline(
        lambda t: t.strip(),
        lambda t: t.lower(),
        lambda t: t.replace(" ", "_")
    )
    print(limpiar_texto("  Hola Mundo Funcional  "))
