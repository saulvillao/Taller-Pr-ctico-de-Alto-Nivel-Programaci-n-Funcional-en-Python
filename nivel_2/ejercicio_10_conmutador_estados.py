# Nivel 2 - Ejercicio 10: Interruptor Múltiple (Máquina de Estados Ligera)
#
# Guarda un índice privado (nonlocal) y lo hace avanzar cíclicamente con el operador módulo,
# alternando entre los estados de una lista interna en cada llamada.

def crear_conmutador(lista_estados):
    indice = -1
    def siguiente():
        nonlocal indice
        indice = (indice + 1) % len(lista_estados)
        return lista_estados[indice]
    return siguiente


if __name__ == "__main__":
    semaforo = crear_conmutador(["rojo", "amarillo", "verde"])
    print(semaforo(), semaforo(), semaforo(), semaforo())  # rojo amarillo verde rojo
