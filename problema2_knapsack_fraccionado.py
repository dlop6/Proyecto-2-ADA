# problema 2: knapsack fraccionado

from dataclasses import dataclass


@dataclass
class Item:
    nombre: str
    precio_total: float
    unidades: float

    @property
    def valor_por_unidad(self):
        # si no hay unidades, no se puede calcular una razon valida
        if self.unidades <= 0:
            raise ValueError("las unidades deben ser positivas")

        return self.precio_total / self.unidades


def knapsack_fraccionado(items, capacidad):
    # la mochila no puede tener capacidad negativa
    if capacidad < 0:
        raise ValueError("la capacidad no puede ser negativa")

    # ordenamos por lo que mas valor da por cada unidad de peso
    ordenados = sorted(items, key=lambda item: item.valor_por_unidad, reverse=True)

    restante = capacidad
    seleccion = []
    valor_total = 0.0

    for item in ordenados:
        if restante == 0:
            break

        # si cabe completo, se toma completo; si no, se toma una fraccion
        unidades_tomadas = min(item.unidades, restante)
        valor_obtenido = unidades_tomadas * item.valor_por_unidad

        seleccion.append({
            "item": item.nombre,
            "unidades_tomadas": unidades_tomadas,
            "valor_por_unidad": item.valor_por_unidad,
            "valor_obtenido": valor_obtenido,
        })

        valor_total += valor_obtenido
        restante -= unidades_tomadas

    return seleccion, valor_total


def imprimir_resultado(numero_caso, items, capacidad):
    seleccion, valor_total = knapsack_fraccionado(items, capacidad)

    print(f"caso {numero_caso}")
    print(f"capacidad = {capacidad}")

    for parte in seleccion:
        print(
            f"tomar {parte['unidades_tomadas']} unidad(es) de {parte['item']} | "
            f"valor/u = {parte['valor_por_unidad']:.2f} | "
            f"subtotal = {parte['valor_obtenido']:.2f}"
        )

    print(f"valor total = {valor_total:.2f}")
    print("-" * 40)


if __name__ == "__main__":
    # estos son los tres casos usados en el documento
    casos = [
        (
            [Item("item 1", 60, 10), Item("item 2", 100, 20), Item("item 3", 120, 30)],
            50,
        ),
        (
            [Item("item 1", 100, 20), Item("item 2", 60, 10)],
            10,
        ),
        (
            [Item("item 1", 45, 15), Item("item 2", 40, 10), Item("item 3", 30, 10)],
            15,
        ),
    ]

    for numero_caso, (items, capacidad) in enumerate(casos, start=1):
        imprimir_resultado(numero_caso, items, capacidad)
