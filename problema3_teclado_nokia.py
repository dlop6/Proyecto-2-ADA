# problema 3: combinaciones en teclado nokia

# cada digito incluye sus vecinos y tambien a si mismo
# se incluye la misma tecla porque el apendice acepta casos como 00, 11 y 22
VECINOS = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [2, 1, 3, 5],
    3: [3, 2, 6],
    4: [4, 1, 5, 7],
    5: [5, 2, 4, 6, 8],
    6: [6, 3, 5, 9],
    7: [7, 4, 8],
    8: [8, 5, 7, 9, 0],
    9: [9, 6, 8],
}


def contar_combinaciones(n):
    # n debe ser positivo porque se piden combinaciones de longitud n
    if n <= 0:
        raise ValueError("n debe ser positivo")

    # para longitud 1, cada digito valido aporta una combinacion
    dp = {digito: 1 for digito in range(10)}

    # construimos las longitudes siguientes usando los resultados anteriores
    for longitud in range(2, n + 1):
        nuevo = {}

        for digito in range(10):
            nuevo[digito] = sum(dp[vecino] for vecino in VECINOS[digito])

        dp = nuevo

    total = sum(dp.values())
    return total, dp


if __name__ == "__main__":
    # estos son los tres casos usados en el documento
    casos = [1, 2, 3]

    for numero_caso, n in enumerate(casos, start=1):
        total, por_digito = contar_combinaciones(n)

        print(f"caso {numero_caso}")
        print(f"n = {n}")
        print(f"total combinaciones = {total}")
        print(f"terminaciones por digito = {por_digito}")
        print("-" * 40)
