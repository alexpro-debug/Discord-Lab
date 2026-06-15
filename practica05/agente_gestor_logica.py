# agente_gestor_logica.py

import discord
import os
from dotenv import load_dotenv
# Importamos la función principal de tu archivo de lógica
from practica03.agente_logica import analizar_comando

# --- CONFIGURACIÓN DE DISCORD ---

# Cargar las variables de entorno (el TOKEN)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los permisos necesarios para leer los mensajes
intents = discord.Intents.default()
intents.message_content = True  

# Crear el cliente del bot
client = discord.Client(intents=intents)

# Evento: Cuando el bot se conecta y está listo
@client.event
async def on_ready():
    print(f'Bot encendido y sincronizado como {client.user}')
    print('Listo para procesar comandos de lógica estructurada V2...')
    print('------')

# Evento: Cuando alguien escribe un mensaje en el servidor
@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo y cicle infinitamente
    if message.author == client.user:
        return
    
    # Imprimir en la consola local qué mensaje llegó
    print(f"Mensaje recibido de {message.author}: {message.content}")

    # Procesamiento: Verificamos si es un comando (empieza con !)
    if message.content.startswith('!'):
        
        # Llamamos a TU función de lógica importada
        # Pasamos el mensaje completo para que tu código lo separe
        resultado = analizar_comando(message.content)

        print(f"Respuesta generada: {resultado}")
        print("-" * 20)
        
        # El bot escribe el resultado de vuelta en el canal de Discord
        await message.channel.send(f"🤖 **Bot:** {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR FATAL: No se encontró la variable DISCORD_TOKEN en el archivo .env")