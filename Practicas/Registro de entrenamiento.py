import statistics
Historial_errores = []
Umbral_convergencia = float(0.50)


def REGISTRAR_EPOCA(self,valor_error):
    if valor_error < Umbral_convergencia and valor_error >= 0:
        print("[SISTEMA] entrenamiento completado: se alcanzó el objetivo de presición")
        Historial_errores.append(valor_error)


while len(Historial_errores) < 5:
    try:
        valor_error = float(input("Ingresa el valor del error para 5 epocas distintas: "))
        REGISTRAR_EPOCA(None, valor_error)
    except ValueError:
        print("Error: el valor ingresado no es un número válido.")
    if valor_error < 0:
        print("Error: el valor del error no puede ser negativo.") 
    if len(Historial_errores) == 5:
        print("Historial de errores:", Historial_errores)       
        # Calculo del promedio de errores
        promedio_error = statistics.mean(Historial_errores)
        print("Promedio de errores:", promedio_error)
        print("El mejor error fue:", min(Historial_errores))



def main():
    pass    

if __name__ == "__main__":    
    
    main()