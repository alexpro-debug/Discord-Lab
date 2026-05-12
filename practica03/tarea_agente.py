import datetime

def agregar_tareas(lista_tareas,descripcion):
    """
    agregar una tarea a la lista si cumle con los requisitos
    """
    
    if len(descripcion )< 3:
        return "Erro: Longitud no valida"
    
    # crear formato para tarea
    fecha = datetime.datetime.now().strftime("%H:%M")
    nueva_tarea = f"{descripcion} - {fecha}"
    lista_tareas.append(nueva_tarea)
    return f"Tarea agregada con exito"

def listar_tareas(lista_tareas):
    """
    formatea la lista de tareas para su vizualzacion
    """
    if not lista_tareas:
        return "no hay tareas"
    
    #agraga una variable llamada resultado
    resultado = "listado de tareas: \n"

    #iterar la lista de tareas y formatear la salida
    for i, tarea in enumerate(lista_tareas, start=1):
        resultado += f"{i}. {tarea}\n"
        return resultado
    
    def eliminar_tarea(lista_tarea, indice):
        """
        eleminar una tarea por su numero de indice
        """
        if not indice.isdigit():
            return "Error: El indice debe ser un numero"
        
        indice = int(indice)-1

        #agregamos al logica para preguntar
        #si el elemento esta en la lista y eleminarlo
        if 0 <= indice < len(lista_tarea):
            tarea_eliminada = lista_tarea.pop(indice)
        else:
            return "Error: No existe"
        return f"Tarea eliminada:{tarea_eliminada}"
    
    def main():
        tareas = []
        PREFIJO = "!"
    
        print("Bienvenido al gestor de tareas")
        activa = True
        while activa:
            entrada = input(">>>").strip()

            if not entrada.startswith(PREFIJO):
                print("Error: Comando no reconocido")
                continue

            #Procesamiento de le entrada
            cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
            comando= cuerpo[0].lower()
            argumento= cuerpo [1] if len(cuerpo)> 1 else ""

    #Seleccion de acción
        if comando=="add":
            resultado = agregar_tareas(tareas, argumento)
            print