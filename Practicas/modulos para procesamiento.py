import math


def IMPRIMIR_ENCABEZADO():
    print("==============================================")
    print("   SISTEMA DE SALUD INTELIGENTE")
    print("==============================================\n") 


def CALCULAR_IMC(peso, altura):
    imc = peso / (altura ** 2)
    return imc


def EVALUAR_PRESION(presion_sistolica):
    if presion_sistolica > 140:
        estado = ("ALTA")
    else:        
        estado = ("NORMAL")
    return estado

def main():
    IMPRIMIR_ENCABEZADO()
    Nombre= input("Ingresa tu nombre: ")
    Peso= float(input("Ingresa tu peso (kg): "))
    Altura= float(input("Ingresa tu altura (m): "))
    IMC= CALCULAR_IMC(Peso, Altura)
    Presion = float(input("Ingresa tu presión sistólica (mmHg): "))
    estado = EVALUAR_PRESION(Presion)
    

    # se impreme el resumen de los datos ingresados y calculados mas el estado de la presión sistólica basandose en NORMAL O ALTA.

    RESUMEN = print("tu nombre es: ", Nombre,   "tu IMC es: ", math.ceil(IMC  ),    "y tu presión sistólica es: ",Presion, "lo que indica que tu presión es: ", estado)


if __name__ == "__main__":  
    main()