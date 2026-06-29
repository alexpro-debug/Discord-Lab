# tools/memoria.py

# Diccionario global que vivirá en la memoria del servidor (Stateful)
# Llave: ID del usuario (Discord) -> Valor: Perfil de aprendizaje
memoria_estado = {}

def obtener_perfil(usuario_id: str) -> dict:
    """Recupera el perfil del alumno, o crea uno nuevo si es su primera vez."""
    if usuario_id not in memoria_estado:
        # Estado inicial del alumno en su primer mensaje
        memoria_estado[usuario_id] = {
            "historial_temas": [],
            "errores_sintaxis": 0
        }
    return memoria_estado[usuario_id]

def registrar_interaccion(usuario_id: str, intencion: str):
    """Guarda la intención en el historial del alumno para darle contexto."""
    perfil = obtener_perfil(usuario_id)
    
    # Solo guardamos si detectó una intención válida (que no sea 'desconocido')
    if intencion != "desconocido":
        perfil["historial_temas"].append(intencion)
        
        # Mantenemos solo los últimos 5 temas para no saturar la memoria RAM
        if len(perfil["historial_temas"]) > 5:
            perfil["historial_temas"].pop(0)

def registrar_error(usuario_id: str):
    """Suma un punto al contador de errores del alumno y devuelve el total."""
    perfil = obtener_perfil(usuario_id)
    perfil["errores_sintaxis"] += 1
    return perfil["errores_sintaxis"]