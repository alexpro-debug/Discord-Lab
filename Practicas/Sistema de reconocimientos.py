"""
Implementar en Python un sistema de reconocimiento de seguridad
siguiendo la lógica definida en el planteamiento.
"""


def reconocimiento_seguridad():
    # Patrón maestro almacenado en la base de datos
    patron_maestro = [1, 0, 1, 1, 0]

    # Lista para almacenar la lectura del sensor
    lectura_sensor = []

    print("--- ESCÁNER BIOMÉTRICO DE IA ---")

    # Captura de los 5 bits del usuario
    i = 1
    while i <= 5:
        bit = int(input(f"Ingrese bit {i}: "))
        lectura_sensor.append(bit)
        i += 1

    print("\n> Comparando lectura con base de datos...")

    # Comparación de listas
    coincidencias = 0
    i = 0

    while i < 5:
        if lectura_sensor[i] == patron_maestro[i]:
            coincidencias += 1
        i += 1

    # Cálculo del porcentaje de similitud
    similitud = (coincidencias / 5) * 100

    # Resultados
    print(f"\n> Coincidencias encontradas: {coincidencias}")
    print(f"> Porcentaje de Similitud: {similitud}%")

    # Toma de decisiones
    if similitud == 100:
        print("\nESTADO: ACCESO TOTAL: Identidad Verificada.")

    elif similitud >= 60:
        print("\nESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")

    else:
        print("\nESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")

    # Mostrar listas (reto adicional)
    print("\nDetalle de comparación")
    print("Patrón Maestro :", patron_maestro)
    print("Lectura Sensor :", lectura_sensor)


def main():
    reconocimiento_seguridad()


if __name__ == "__main__":
    main()