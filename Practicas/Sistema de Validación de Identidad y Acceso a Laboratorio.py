"""
El programa simula un sistema de acceso biométrico, solicita datos
del ingeniero y verifica el ID junto con los escaneos de iris y
reconocimiento facial para decidir si el acceso es permitido,
restringido o bloqueado
"""

def acceso_biometrico():
    print("SISTEMA DE CONTROL BIOMÉTRICO")

    # Entrada de datos
    nombre = input("\nNombre del Ingeniero: ")

    id_empleado = int(input("\nID de Empleado: "))

    iris = input(
        "\n¿El escaneo de Iris coincide? (si/no): "
    ).lower()

    facial = input(
        "\n¿El reconocimiento facial es > 95%? (si/no): "
    ).lower()

    # Validación de ID inválido
    if id_empleado <= 0:
        print(
            "\n> Diagnóstico: ¡ALERTA DE SEGURIDAD! "
            "ID inválido detectado. Bloqueando accesos y notificando a la policía."
        )

    # Acceso SENIOR
    elif id_empleado < 100 and iris == "si" and facial == "si":
        print(
            f"\n> Diagnóstico: Bienvenido, Ingeniero {nombre}. "
            "Acceso nivel SENIOR concedido a todas las áreas."
        )

        # reto adicional
        print(
            f"Generando log de entrada para el usuario: {id_empleado}..."
        )

    # Acceso JUNIOR
    elif id_empleado >= 100 and iris == "si" and facial == "si":
        print(
            f"\n> Diagnóstico: Bienvenido, Ingeniero {nombre}. "
            "Acceso nivel JUNIOR concedido. Áreas de servidores restringidas."
        )

        # reto adicional
        print(
            f"Generando log de entrada para el usuario: {id_empleado}..."
        )

    # Fallo biométrico
    else:
        print(
            "\n> Diagnóstico: Error Biométrico: "
            "Identidad no verificada al 100%. "
            "Por favor, contacte a seguridad."
        )


def main():
    acceso_biometrico()


if __name__ == "__main__":
    main()