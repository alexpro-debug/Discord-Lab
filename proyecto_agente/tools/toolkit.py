# tools/toolkit.py

# Importamos las funciones puras desde la carpeta de módulos
from modulos.logica_pedagogica import (
    explicar_tipo_dato,
    evaluar_ciclo_while,
    operar_lista,
    simular_try_except
)

# Este es el catálogo centralizado. 
# La llave ("explicar_tipo", etc.) DEBE ser exactamente la misma que devuelve el clasificador.py
TOOLKIT = {
    "explicar_tipo": {
        "funcion": explicar_tipo_dato,
        "descripcion": "explicación sobre los tipos de datos en Python"
    },
    "revisar_while": {
        "funcion": evaluar_ciclo_while,
        "descripcion": "revisión de la estructura de tu ciclo while"
    },
    "metodo_lista": {
        "funcion": operar_lista,
        "descripcion": "demostración de cómo alterar una lista"
    },
    "dividir_seguro": {
        "funcion": simular_try_except,
        "descripcion": "lección sobre manejo de excepciones al dividir"
    }
}