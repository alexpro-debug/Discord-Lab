"""
Implementar un analizador básico de sentimientos
siguiendo la lógica definida en el planteamiento.
"""


def analizador_sentimientos():
    # Vector de características:
    # [0] Positivo
    # [1] Neutral
    # [2] Negativo
    puntajes_sentimiento = [0, 0, 0]

    print("--- ANALIZADOR DE SENTIMIENTOS IA ---")

    # Lectura de las 5 palabras
    for i in range(5):
        clasificacion = int(
            input(f"\nPalabra {i + 1} - Clasificación (0, 1, 2): ")
        )

        # Incrementar la posición correspondiente
        puntajes_sentimiento[clasificacion] += 1

    # Mostrar vector final
    print("\nEstado final del vector de características:")
    print(puntajes_sentimiento)

    # Buscar manualmente el valor mayor
    mayor = puntajes_sentimiento[0]
    indice_mayor = 0

    i = 1

    while i < 3:
        if puntajes_sentimiento[i] > mayor:
            mayor = puntajes_sentimiento[i]
            indice_mayor = i

        i += 1

    # Resultado final
    if indice_mayor == 0:
        print("\nResultado de IA: La frase es Positiva (Predominancia en índice 0)")

    elif indice_mayor == 1:
        print("\nResultado de IA: La frase es Neutral (Predominancia en índice 1)")

    else:
        print("\nResultado de IA: La frase es Negativa (Predominancia en índice 2)")


def main():
    analizador_sentimientos()


if __name__ == "__main__":
    main()