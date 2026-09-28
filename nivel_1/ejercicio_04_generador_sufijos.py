# Nivel 1 - Ejercicio 4: Generador de Seriales / Nombres Únicos
#
# Combina una lambda de formato con estado interno privado (un contador que se incrementa
# con nonlocal). Cada llamada genera un nombre distinto sin exponer el contador al exterior.

def crear_generador_sufijos(patron_lambda):
    contador = 0
    def generar(nombre):
        nonlocal contador
        contador += 1
        return patron_lambda(nombre, contador)
    return generar


if __name__ == "__main__":
    generar_nombre = crear_generador_sufijos(lambda n, c: f"{n}_v{c}")
    print(generar_nombre("informe"), generar_nombre("informe"), generar_nombre("informe"))
