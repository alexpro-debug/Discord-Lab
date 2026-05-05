def capturar_datos():
    """
    Captura 8 lecturas de temperatura desde el usuario
    y las almacena en una lista.
    """
    temperaturas = []
    
    for i in range(8):
        valor = float(input(f"Lectura {i+1}: "))
        temperaturas.append(valor)
    
    return temperaturas


def filtrar_datos(temperaturas):
    """
    Detecta valores fuera de rango (outliers) y los corrige.
    Retorna la lista corregida y el número de errores.
    """
    contador_errores = 0
    
    for i in range(len(temperaturas)):
        if temperaturas[i] < 0 or temperaturas[i] > 100:
            temperaturas[i] = 35.0
            contador_errores += 1
    
    return temperaturas, contador_errores


def calcular_promedio(temperaturas):
    """
    Calcula el promedio sin usar sum() ni len().
    """
    suma = 0
    contador = 0
    
    for temp in temperaturas:
        suma += temp
        contador += 1
    
    promedio = suma / contador
    return promedio


def evaluar_estado(promedio):
    """
    Aplica la regla de decisión tipo IA.
    """
    if promedio > 75:
        return "ALERTA: Activando sistema de enfriamiento líquido"
    else:
        return "Estado: Operación normal"


def main():
    print("SISTEMA DE FILTRADO DE DATOS (SENSOR GPU)32\n")
    
    # 1. Captura de datos
    temperaturas = capturar_datos()
    
    # 2. Filtrado de datos
    temperaturas_limpias, errores = filtrar_datos(temperaturas)
    
    print(f"\nSe detectaron {errores} lecturas erróneas y fueron corregidas a 35.0.\n")
    
    # 3. Mostrar datos limpios
    print(f"Datos limpios: {temperaturas_limpias}")
    
    # 4. Calcular promedio
    promedio = calcular_promedio(temperaturas_limpias)
    print(f"Promedio de operación: {round(promedio, 2)}°C")
    
    # 5. Evaluación tipo IA
    estado = evaluar_estado(promedio)
    print(estado)


if __name__ == "__main__":
    main()