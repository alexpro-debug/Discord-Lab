def main():
    print("--- TELEMETRÍA DE CLUSTER IA ---")
    
    try:
        # 1. Captura de Telemetría (Entradas)
        temp_gpu = float(input("\nTemperatura actual (°C): "))
        uso_vram = int(input("Uso de Memoria VRAM (%): "))
        
        # 2. Gestión de Errores (Validación de VRAM antes de preguntar lo demás)
        if uso_vram < 0 or uso_vram > 100:
            print("\nError: Lectura de memoria fuera de rango (0-100%).")
            return # Termina la ejecución de la función si hay error
            
        enfriamiento = input("¿Enfriamiento activo? (si/no): ").strip().lower()
        
        print("\n> Diagnóstico: ", end="")
        
        # 3. Lógica de Diagnóstico (Estructuras de Control)
        
        # ESTADO CRÍTICO
        if temp_gpu > 90.0 or uso_vram == 100:
            print("¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")
            
        # ESTADO DE PRECAUCIÓN
        elif 75.0 <= temp_gpu <= 90.0:
            if enfriamiento == "no":
                print("Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
            elif enfriamiento == "si" or enfriamiento == "sí":
                print("Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
            else:
                print("Error en lectura de sistema de enfriamiento.")
                
        # ESTADO ÓPTIMO
        elif temp_gpu < 75.0 and uso_vram < 80:
            print("Sistema Estable: Entrenamiento en curso a máxima capacidad.")
            
            # 4. Reto Adicional (Opcional)
            vram_libre = 100 - uso_vram
            print(f"\n   [Info para el Ingeniero]: Queda un {vram_libre}% de memoria VRAM libre.")
            print("   Es posible cargar otro modelo de IA en paralelo sin saturar el servidor.")
            
        else:
            # Captura cualquier otro estado que no caiga en las reglas (ej. temp < 75 pero VRAM en 95%)
            print("Sistema en estado de alerta moderada. Monitoreando variaciones.")

    except ValueError:
        # Esto evita que el programa se rompa si el usuario teclea letras en lugar de números
        print("\n[ERROR] Entrada no válida. Debes ingresar valores numéricos para la temperatura y la VRAM.")

# ==========================================
# Ejecución Principal
# ==========================================
if __name__ == "__main__":
    main()