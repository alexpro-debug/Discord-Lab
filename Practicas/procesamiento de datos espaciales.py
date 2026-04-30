"""
==========================================
 Funciones del Sistema
==========================================
"""

def procesar_sensores():
    """Parte 1: Manejo del vector de proximidad (1D)"""
    print("--- MÓDULO DE SENSORES (VECTORES) ---")
    
    sensores_distancia = [0.0] * 5
    
    for i in range(5):
        sensores_distancia[i] = float(input(f"Ingrese distancia sensor {i+1}: "))
    
    promedio = sum(sensores_distancia) / len(sensores_distancia)
    
    print(f"\nPromedio de proximidad: {promedio:.1f}m. ", end="")
    if promedio < 2.0:
        print("Estado: Aviso: Reduciendo velocidad global.")
    else:
        print("Estado: Seguro.")
    print("\n")


def procesar_camara():
    """Parte 2: Llenado y visualización de la matriz de visión (2D)"""
    print("--- MÓDULO DE VISIÓN (MATRICES) ---")
    print("Llenando matriz de cámara 3x3:\n")
    
    camara_ia = [[0, 0, 0], 
                 [0, 0, 0], 
                 [0, 0, 0]]
    
    for fila in range(3):
        for columna in range(3):
            brillo = int(input(f"Fila {fila}, Col {columna} (Brillo 0-255): "))
            
            #Operación de saturación
            if brillo > 255:
                brillo = 255
            elif brillo < 0:
                brillo = 0
                
            camara_ia[fila][columna] = brillo
    
    print("\nVisualización de la imagen capturada:")
    for fila in range(3):
        print("[", end=" ")
        for columna in range(3):
            print(f"{camara_ia[fila][columna]} ", end="")
        print("]")
        
    return camara_ia #Retornamos la matriz para que la siguiente función la pueda usar


def analizar_brillo(matriz):
    """Parte 3: Operaciones sobre la matriz para detectar luz alta"""
    puntos_luz_alta = 0
    
    for fila in range(3):
        for columna in range(3):
            if matriz[fila][columna] > 200:
                puntos_luz_alta += 1
                
    print("\nResultado de Análisis IA:")
    print(f"Se detectaron {puntos_luz_alta} píxeles de alta intensidad.")


"""
==========================================
Ejecución Principal
==========================================
"""
def main():
    #Ejecutamos el módulo de sensores
    procesar_sensores()
    
    #Ejecutamos la cámara y guardamos la matriz que nos devuelve
    matriz_generada = procesar_camara()
    
    #Le pasamos la matriz generada a la función de análisis
    analizar_brillo(matriz_generada)


if __name__ == "__main__":
    main()