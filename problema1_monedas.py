# problema 1: cambio de monedas con denominaciones canonicas

def hacer_sencillo(monto_centavos, monedas=(25, 10, 5, 1)):
    # revisamos que el monto tenga sentido antes de calcular
    if monto_centavos < 0:
        raise ValueError("el monto no puede ser negativo")

    resultado = {}
    restante = monto_centavos

    # tomamos primero las monedas mas grandes posibles
    for moneda in monedas:
        cantidad = restante // moneda
        resultado[moneda] = cantidad
        restante = restante % moneda

    total_monedas = sum(resultado.values())
    return resultado, total_monedas


def formatear_cambio(resultado):
    # solo mostramos las monedas que si se usaron
    partes = []

    for moneda, cantidad in resultado.items():
        if cantidad > 0:
            partes.append(f"{cantidad} moneda(s) de {moneda}")

    return ", ".join(partes) if partes else "sin monedas"


if __name__ == "__main__":
    # estos son los tres casos usados en el documento
    casos = [293, 68, 99]

    for numero_caso, monto in enumerate(casos, start=1):
        cambio, total = hacer_sencillo(monto)

        print(f"caso {numero_caso}")
        print(f"monto = {monto} centavos")
        print(f"cambio = {formatear_cambio(cambio)}")
        print(f"total monedas = {total}")
        print("-" * 40)
