# Nivel 1 - Ejercicio 1: Generador de Formateadores con Transformación
#
# HOF que recibe una lambda de transformación (fn_transformacion) y retorna un closure.
# El closure 'recuerda' el prefijo y la transformación recibidos, aplicándolos cada vez
# que se le pasa un nuevo texto.

def crear_formateador(prefijo, fn_transformacion):
    def formateador(texto):
        return f"{prefijo}{fn_transformacion(texto)}"
    return formateador


if __name__ == "__main__":
    formateador_mayus = crear_formateador(">> ", lambda t: t.upper())
    print(formateador_mayus("hola mundo"))  # >> HOLA MUNDO
