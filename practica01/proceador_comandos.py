import datetime

def obtener_saludo(nombre_bot):
    """
    Retorna un saludo formateado
    """
    return f"¡Hola! Soy {nombre_bot} y estoy lista para ayudarte."
    
def procesar_comando_recordar(comando):
    """
    Valida y procesa la accion de recirdar un dato
    """
    if not comando:
        return"Error: falta el nombre. Uso !recordar [nombre]"
    return f"¡He recordado el nombre '{comando}'"
    
def calcular_uptime(hora_inicio):
    """
    calcula la diferencia de tiempo entre el inicio
    y el actual (mostrar actividad del bot)
    """
    ahora=datetime.datetime.now()
    diferencia=ahora-hora_inicio
    segundos=int(diferencia.total_seconds())
    return f"tiempo de actividad: {segundos} segundos"

def mostrar_ayuda():
    """
    comandos disponibles para el usuario
    """
    return(
        "Comandos disponibles:\n"
        "!saludo - muestra un saludo del bot\n"
        "!recordar [nombre] - el bot recordadra el nombre proporcionad\n"
        "!uptime - muestra el tiempo de actividad del bot\n"
        "!ayuda - muestra esta lista de comandos"
        "!salir - termina la actividad del bot"
    )

    
def iniciar_agente():
    NOMBRE_BOT = "Nekotina 2"
    PREFIJO = "!"
    hora_inicio =  datetime.datetime.now()

    print(f"{obtener_saludo(NOMBRE_BOT)}")
    print("escribe !ayuda para ver los comandos disponibles.")

    ejecutando = True
    while ejecutando:
        entrada = input(f"[{NOMBRE_BOT}] Ingrese comando: ").strip()

        if not entrada.startswith(PREFIJO):
            print("Comando no reconocido.")
            continue
        
        partes = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = partes[0].lower()
        argumento = partes[1] if len(partes) > 1 else ""

        if comando == "saludo":
            print(obtener_saludo(NOMBRE_BOT))
        elif comando == "ayuda":
            print(mostrar_ayuda())
        else:
            print("Comando no reconocido.")                         


def main():
    iniciar_agente()
    

if __name__ == "__main__":
    main()