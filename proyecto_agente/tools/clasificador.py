# tools/clasificador.py
import re

def clasificar_intencion(texto_usuario: str) -> str:
    """
    Recibe texto en lenguaje natural y devuelve la intención detectada (la llave del toolkit).
    """
    # Convertimos todo a minúsculas para que sea más fácil buscar
    texto = texto_usuario.lower()

    # 1. Intención: Explicar tipo de dato
    # Busca combinaciones como "explicame... float" o "que son... variables"
    if re.search(r'\b(que son|explicame|dime de).*(variables|float|int|string|datos)\b', texto):
        return "explicar_tipo"

    # 2. Intención: Revisar ciclo while
    # Busca "revisa... codigo" o directamente la palabra "while"
    elif re.search(r'\b(revisa|checa|mira).*(codigo|while|ciclo)\b', texto) or "while " in texto:
        return "revisar_while"

    # 3. Intención: Métodos de lista
    elif re.search(r'\b(ejemplo|como usar).*(append|pop|listas|arreglos)\b', texto):
        return "metodo_lista"

    # 4. Intención: Dividir seguro (Try-Except)
    elif re.search(r'\b(por que truena|error|dividir|cero|0)\b', texto):
        return "dividir_seguro"

    # Si el bot no detecta ninguna palabra clave de su temario
    return "desconocido"