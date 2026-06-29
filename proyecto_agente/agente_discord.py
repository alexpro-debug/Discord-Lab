# agente_discord.py
import discord
import os
import re
from dotenv import load_dotenv

# Importamos las herramientas de nuestra arquitectura modular (Capa de Decisión)
from tools.clasificador import clasificar_intencion
from tools.memoria import registrar_interaccion, obtener_perfil, registrar_error
from tools.toolkit import TOOLKIT

# --- CONFIGURACIÓN DE DISCORD ---
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True  
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Agente Cognitivo conectado exitosamente como {client.user}')
    print('Esperando dudas de los alumnos en lenguaje natural...')
    print('-' * 30)

@client.event
async def on_message(message):
    # 1. PERCEPCIÓN
    # Evitamos que el bot se responda a sí mismo y cicle el universo
    if message.author == client.user:
        return
    
    texto_usuario = message.content
    usuario_id = str(message.author.id)

    # 2. PENSAMIENTO (Clasificación NLP)
    intencion = clasificar_intencion(texto_usuario)
    
    # Guardamos el tema en la memoria de estado del alumno
    registrar_interaccion(usuario_id, intencion)
    perfil = obtener_perfil(usuario_id)

    print(f"[LOG] Usuario: {message.author.name} | Intención: {intencion} | Historial en memoria: {perfil['historial_temas']}")

    # Si no entendió, responde con empatía
    if intencion == "desconocido":
        respuesta = "🤖 **Agente Tutor:** Aún estoy aprendiendo. Intenta preguntarme sobre variables, tipos de datos, revisar un ciclo while, o cómo usar listas."
        await message.channel.send(respuesta)
        return

    # 3. ACCIÓN (Ejecución de la Caja de Herramientas)
    herramienta = TOOLKIT[intencion]["funcion"]
    descripcion = TOOLKIT[intencion]["descripcion"]

    # --- Preparamos los argumentos según lo que pida la herramienta ---
    if intencion == "dividir_seguro":
        # Extraemos los números del texto del usuario usando expresiones regulares
        numeros = re.findall(r'\d+', texto_usuario)
        if len(numeros) >= 2:
            resultado = herramienta(numeros[0], numeros[1]) # Le mandamos num1 y num2
        else:
            resultado = "⚠️ Necesito dos números en tu frase para simular la división (ej. 'divide 10 entre 0')."
    else:
        # Para las demás, les pasamos todo el texto y ellas solitas extraen lo que necesitan
        resultado = herramienta(texto_usuario)

    # --- INTERVENCIÓN PEDAGÓGICA BASADA EN MEMORIA (El toque maestro) ---
    # Si el bot atrapó un error grave (como un ciclo infinito o dividir por cero)
    if "ALERTA" in resultado or "Boom" in resultado:
        errores_totales = registrar_error(usuario_id)
        
        # Si el alumno se ha equivocado 2 veces o más, el bot interviene
        if errores_totales >= 2:
            resultado += f"\n\n💡 **Nota del Tutor:** He notado en tu historial que te has equivocado {errores_totales} veces probando excepciones o ciclos. Recuerda repasar la teoría de Programación Estructurada con calma, ¡no te rindas!"

    # Enviamos la respuesta final al canal
    respuesta_final = f"🤖 **Agente Tutor** (Te estoy dando {descripcion}):\n\n{resultado}"
    await message.channel.send(respuesta_final)


# --- ARRANQUE DEL BOT ---
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("🚨 ERROR FATAL: No encontré el DISCORD_TOKEN. Verifica tu archivo .env")