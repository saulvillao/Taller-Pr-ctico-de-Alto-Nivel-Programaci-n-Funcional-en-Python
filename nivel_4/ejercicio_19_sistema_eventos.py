# Nivel 4 - Ejercicio 19: Sistema Pub/Sub (Event Listener con HOFs y Closures)
#
# Implementa el patrón publicador/suscriptor: el closure 'gestor' mantiene un diccionario
# privado de suscriptores (lambdas) y, al emitir un evento, notifica a cada uno de ellos.

def crear_sistema_eventos():
    suscriptores = {}
    def gestor(accion, evento, *args):
        if accion == "suscribir":
            callback = args[0]
            suscriptores.setdefault(evento, []).append(callback)
            return None
        elif accion == "emitir":
            for callback in suscriptores.get(evento, []):
                callback(*args)
            return None
        else:
            raise ValueError("Acción no soportada: use 'suscribir' o 'emitir'")
    return gestor


if __name__ == "__main__":
    eventos_recibidos = []
    sistema = crear_sistema_eventos()
    sistema("suscribir", "compra", lambda producto: eventos_recibidos.append(f"Compra registrada: {producto}"))
    sistema("suscribir", "compra", lambda producto: print("   [log] Notificación de compra:", producto))
    sistema("emitir", "compra", "Teclado mecánico")
    print(eventos_recibidos)
