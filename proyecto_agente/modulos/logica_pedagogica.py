# modulos/logica_pedagogica.py
import re

# --- TEMA 1: SINTAXIS BÁSICA ---
def explicar_tipo_dato(tipo: str) -> str:
    """Explica los tipos de datos en Python."""
    conceptos = {
        "float": "Un `float` (flotante) es un tipo de dato numérico que incluye decimales. Ejemplo: `pi = 3.1416`",
        "int": "Un `int` (entero) es un número sin decimales. Ejemplo: `edad = 18`",
        "string": "Un `str` (cadena) es texto puro, siempre va entre comillas. Ejemplo: `nombre = 'Jin Kusanagi'`",
        "variables": "Una variable es como una cajita en la memoria de la compu donde guardas datos para usarlos después."
    }
    # Buscamos si la palabra existe en nuestro mini-diccionario
    for clave, explicacion in conceptos.items():
        if clave in tipo.lower():
            return f"📘 **Sintaxis Básica:**\n{explicacion}"
    
    return "📘 **Sintaxis Básica:** Los tipos de datos principales son int (enteros), float (decimales), str (texto) y bool (verdadero/falso)."

# --- TEMA 2: ESTRUCTURAS DE CONTROL ---
def evaluar_ciclo_while(codigo: str) -> str:
    """Evalúa si un ciclo while tiene el riesgo de volverse infinito."""
    # Verificamos si realmente escribió un while
    if "while" not in codigo:
        return "⚠️ Ese código no parece tener un ciclo `while`."
    
    # Buscamos signos de incremento/decremento comunes en Python (+=, -=, =, etc.)
    # Si no hay operaciones matemáticas dentro del ciclo, seguro es infinito
    if not re.search(r'(\+=|-=|=.*[+\-])', codigo):
        return "🚨 **¡ALERTA DE CICLO INFINITO!** 🚨\nVeo un `while`, pero no detecto que estés actualizando tu variable de control (ej. `x += 1`). Si corres esto, tu compu va a crashear."
    
    return "✅ **Estructura de Control:** Tu ciclo `while` se ve bien estructurado. Tienes una condición y actualizas la variable. ¡Vas por buen camino!"

# --- TEMA 3: ESTRUCTURAS DE DATOS ---
def operar_lista(metodo: str) -> str:
    """Simula lo que le pasa a una lista cuando le aplicas un método."""
    metodo = metodo.lower()
    lista_ejemplo = [1, 2, 3]
    
    if "append" in metodo:
        lista_ejemplo.append(99)
        return f"📦 **Estructura de Datos (Listas):**\nEl método `.append(99)` agrega un elemento al final.\nAntes: `[1, 2, 3]`\nDespués: `{lista_ejemplo}`"
    
    elif "pop" in metodo:
        eliminado = lista_ejemplo.pop()
        return f"📦 **Estructura de Datos (Listas):**\nEl método `.pop()` saca y borra el último elemento.\nAntes: `[1, 2, 3]`\nElemento sacado: `{eliminado}`\nDespués: `{lista_ejemplo}`"
    
    return "📦 **Estructura de Datos:** Prueba preguntarme cómo usar `append` o `pop` en listas."

# --- TEMA 4: MANEJO DE EXCEPCIONES ---
def simular_try_except(numerador: str, denominador: str) -> str:
    """Demuestra el flujo defensivo atrapando una división por cero."""
    try:
        # Intentamos convertir los textos a números y dividir
        num1 = float(numerador)
        num2 = float(denominador)
        resultado = num1 / num2
        return f"🛡️ **Manejo de Excepciones:**\nLa división de {num1} / {num2} es: {resultado}. No hubo errores, el programa sigue normal."
        
    except ZeroDivisionError:
        return "🛡️ **Manejo de Excepciones:**\n¡Boom! Intentaste dividir entre cero. Esto colapsaría un programa normal, pero gracias al bloque `except ZeroDivisionError`, el error fue atrapado y tu bot sigue vivo."
    except ValueError:
        return "🛡️ **Manejo de Excepciones:**\n¡Error de valor! Asegúrate de darme números de verdad."