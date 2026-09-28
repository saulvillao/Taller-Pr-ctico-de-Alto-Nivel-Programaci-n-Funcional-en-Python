# Nivel 1 - Ejercicio 5: Conversor de Divisas con Margen
#
# El closure encapsula una tasa de cambio fija y usa una lambda para calcular dinámicamente
# la comisión/margen sobre el monto ya convertido.

def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        convertido = monto * tasa
        comision = margen_lambda(convertido)
        return round(convertido - comision, 2)
    return convertir


if __name__ == "__main__":
    conversor_usd_eur = crear_conversor(0.92, lambda monto: monto * 0.03)
    print(conversor_usd_eur(100))  # 89.24
