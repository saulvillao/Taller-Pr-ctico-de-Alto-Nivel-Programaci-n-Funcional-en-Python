# Nivel 2 - Ejercicio 6: Contador Ponderado
#
# Usa 'nonlocal' para mutar la variable privada 'cuenta' en cada llamada. La regla de
# incremento no está fija en el código: se delega por completo a la lambda fn_paso.

def crear_contador_paso(fn_paso):
    cuenta = 0
    def contar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return contar


if __name__ == "__main__":
    contador = crear_contador_paso(lambda c: c + 5)
    print(contador(), contador(), contador())  # 5 10 15
