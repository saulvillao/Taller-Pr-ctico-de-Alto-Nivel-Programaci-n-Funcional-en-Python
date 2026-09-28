# Nivel 1 - Ejercicio 3: Calculador de Descuentos con Regla Dinámica
#
# La lambda actúa como 'regla de negocio' que decide si corresponde aplicar el descuento.
# El closure encapsula el porcentaje de descuento a aplicar cuando la regla se cumple.

def crear_descuento_dinamico(regla_condicional_lambda, porcentaje_descuento=0.10):
    def calcular(precio):
        if regla_condicional_lambda(precio):
            return round(precio * (1 - porcentaje_descuento), 2)
        return precio
    return calcular


if __name__ == "__main__":
    descuento_vip = crear_descuento_dinamico(lambda p: p > 100, 0.20)
    print(descuento_vip(150), descuento_vip(50))  # 120.0 50
