# Nivel 4 - Ejercicio 17: Caché con Expiración o Tamaño Máximo (Memoización Profesional)
#
# El closure mantiene una caché privada tipo LRU (OrderedDict). Cuando se supera max_items
# descarta el elemento más antiguo, evitando así recalcular fn_costosa innecesariamente.

from collections import OrderedDict

def memoizar_avanzado(fn_costosa, max_items):
    cache = OrderedDict()
    def memoizada(*args):
        if args in cache:
            cache.move_to_end(args)
            return cache[args]
        resultado = fn_costosa(*args)
        cache[args] = resultado
        if len(cache) > max_items:
            cache.popitem(last=False)  # descarta el más antiguo
        return resultado
    return memoizada


if __name__ == "__main__":
    llamadas_reales = [0]

    def cuadrado_costoso(n):
        llamadas_reales[0] += 1
        return n * n

    cuadrado_memo = memoizar_avanzado(cuadrado_costoso, max_items=2)
    print(cuadrado_memo(4), cuadrado_memo(5), cuadrado_memo(4), cuadrado_memo(6))
    print("Llamadas reales:", llamadas_reales[0])
