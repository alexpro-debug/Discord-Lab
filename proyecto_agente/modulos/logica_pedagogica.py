# modulos/logica_pedagogica.py
import re

# --- TEMA 1: SINTAXIS BÁSICA ---
def explicar_tipo_dato(tipo: str) -> str:
    """Explica los tipos de datos en Python."""
    conceptos = {
        "float": "Un 'float' (flotante) es un tipo de dato numérico que incluye decimales. Ejemplo: pi = 3.1416",
        "int": "Un 'int' (entero) es un número sin decimales. Ejemplo: edad = 18",
        "string": "Un 'str' (cadena) es texto puro, siempre va entre comillas. Ejemplo: nombre = 'Jin Kusanagi'",
        "variables": "Una variable es un espacio reservado en la memoria que almacena un valor que puede cambiar durante la ejecución."
    }
    
    for clave, explicacion in conceptos.items():
        if clave in tipo.lower():
            return f"[Sintaxis Básica] -> {explicacion}"
    
    return "[Sintaxis Básica] -> Los tipos de datos principales son int (enteros), float (decimales), str (texto) y bool (verdadero/falso)."

# --- TEMA 2: ESTRUCTURAS DE CONTROL ---
def evaluar_ciclo_while(codigo: str) -> str:
    """Evalúa si un ciclo while tiene el riesgo de volverse infinito."""
    if "while" not in codigo:
        return "[Aviso] -> El bloque de código proporcionado no contiene la estructura 'while'."
    
    if not re.search(r'(\+=|-=|=.*[+\-])', codigo):
        return "[ALERTA DE SEGURIDAD] -> Posible ciclo infinito detectado. No se encontró la actualización de la variable de control (ej. x += 1). Ejecutar esto consumirá los recursos del sistema."
    
    return "[OK] -> Estructura de control validada. El ciclo 'while' contiene una condición y actualización de variable."

# --- TEMA 3: ESTRUCTURAS DE DATOS ---
def operar_lista(metodo: str) -> str:
    """Simula lo que le pasa a una lista cuando le aplicas un método."""
    metodo = metodo.lower()
    lista_ejemplo = [1, 2, 3]
    
    if "append" in metodo:
        lista_ejemplo.append(99)
        return f"[Listas] -> El método .append(99) inserta un elemento al final de la estructura.\n>>> Estado anterior: [1, 2, 3]\n>>> Estado actual:   {lista_ejemplo}"
    
    elif "pop" in metodo:
        eliminado = lista_ejemplo.pop()
        return f"[Listas] -> El método .pop() extrae y elimina el último elemento.\n>>> Estado anterior: [1, 2, 3]\n>>> Elemento extraído: {eliminado}\n>>> Estado actual:     {lista_ejemplo}"
    
    return "[Listas] -> Puedes solicitar demostraciones de los métodos 'append' o 'pop'."

# --- TEMA 4: MANEJO DE EXCEPCIONES ---
def simular_try_except(numerador: str, denominador: str) -> str:
    """Demuestra el flujo defensivo atrapando una división por cero."""
    try:
        num1 = float(numerador)
        num2 = float(denominador)
        resultado = num1 / num2
        return f"[Excepciones] -> Operación exitosa. {num1} / {num2} = {resultado}. El flujo del programa continúa normalmente."
        
    except ZeroDivisionError:
        return "[Excepciones] -> Excepción 'ZeroDivisionError' capturada. Se intentó dividir entre cero, pero el bloque 'except' evitó la terminación abrupta del programa."
    except ValueError:
        return "[Excepciones] -> Excepción 'ValueError' capturada. Los argumentos proporcionados no son numéricos."