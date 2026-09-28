# Nivel 3 - Ejercicio 14: Compositor de Cadenas de Operaciones
#
# Closure clásico de composición matemática de funciones: f(g(x)). Permite encadenar dos
# transformaciones (lambdas o funciones) en una sola función reutilizable.

def componer_dos(f, g):
    def compuesta(x):
        return f(g(x))
    return compuesta


if __name__ == "__main__":
    combinada = componer_dos(lambda x: x * 2, lambda x: x + 3)
    print(combinada(5))  # (5+3)*2 = 16
