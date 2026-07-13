# agente_discord.py
import discord
import os
import re
from dotenv import load_dotenv

# Importamos las herramientas de nuestra arquitectura modular
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
    print(f'[INFO] Agente Cognitivo inicializado y conectado como {client.user}')
    print('[INFO] A la espera de instrucciones en lenguaje natural...')
    print('-' * 40)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    texto_usuario = message.content
    usuario_id = str(message.author.id)

    # 2. PENSAMIENTO (Clasificación NLP)
    intencion = clasificar_intencion(texto_usuario)
    
    # Guardamos el tema en la memoria de estado
    registrar_interaccion(usuario_id, intencion)
    perfil = obtener_perfil(usuario_id)

    print(f"[LOG] Usuario: {message.author.name} | Intención: {intencion} | Historial: {perfil['historial_temas']}")

    if intencion == "desconocido":
        respuesta = "**[Agente Tutor]**\n```text\n[Aviso] -> Instrucción no reconocida. Intente consultar sobre variables, tipos de datos, ciclos while o listas.\n```"
        await message.channel.send(respuesta)
        return

    # 3. ACCIÓN (Ejecución de la Caja de Herramientas)
    herramienta = TOOLKIT[intencion]["funcion"]
    descripcion = TOOLKIT[intencion]["descripcion"]

    if intencion == "dividir_seguro":
        numeros = re.findall(r'\d+', texto_usuario)
        if len(numeros) >= 2:
            resultado = herramienta(numeros[0], numeros[1])
        else:
            resultado = "[Aviso] -> Se requieren dos números en la instrucción para simular la división."
    else:
        resultado = herramienta(texto_usuario)

    # --- INTERVENCIÓN PEDAGÓGICA BASADA EN MEMORIA ---
    if "ALERTA" in resultado or "capturada" in resultado:
        errores_totales = registrar_error(usuario_id)
        
        if errores_totales >= 2:
            resultado += f"\n\n[Nota del Sistema Tutor] -> Se han registrado {errores_totales} errores críticos en su sesión actual. Se recomienda revisar la documentación de Programación Estructurada para evitar fallos lógicos."

    # Enviamos la respuesta final al canal empaquetada en un bloque de código
    respuesta_final = f"**[Módulo de ejecución: {descripcion.capitalize()}]**\n```text\n{resultado}\n```"
    await message.channel.send(respuesta_final)

if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("[ERROR FATAL] No se encontró el DISCORD_TOKEN en el archivo .env")