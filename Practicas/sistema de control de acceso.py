class ControlAcceso:
    def __init__(self):
        #Atributo: diccionario con al menos 3 registros iniciales
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        #Lógica de validación
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            #Imprimimos el mensaje exacto que pide el ejemplo de ejecución
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")
            return None

    def agregar_usuario(self, nueva_matricula, nuevo_rol):
        #Funcionalidad extra: Agregar nuevos usuarios al diccionario
        self.usuarios_autorizados[nueva_matricula] = nuevo_rol
        print(f"> [SISTEMA] Usuario {nueva_matricula} registrado exitosamente como {nuevo_rol}.")


def main():
    print("--- Sistema de Seguridad Laboratorio IA - UX ---")
    
    #Instanciamos nuestra clase
    sistema_ux = ControlAcceso()
    
    #Ciclo de Gestión (Bucle infinito hasta que el usuario decida salir)
    while True:
        print("\n" + "="*50 + "\n")
        
        try:
            matricula = input("Ingrese su matrícula (o 'salir' para apagar): ").strip()
            
            #Condición para romper el bucle y terminar el programa
            if matricula.lower() == 'salir':
                print("Apagando sistema...")
                break
                
            #Captura de error si el campo se deja vacío
            if matricula == "":
                raise ValueError("El campo de matrícula no puede estar vacío.")
                
            #Llamamos al método de validación
            rol_actual = sistema_ux.verificar_permisos(matricula)
            
            #Funcionalidad Extra: Si es Administrador, le damos la opción de agregar a alguien
            if rol_actual == "Administrador":
                opcion = input("\n[ADMIN] ¿Desea registrar un nuevo usuario? (s/n): ").strip().lower()
                if opcion == 's':
                    nueva_mat = input("[ADMIN] Ingrese la nueva matrícula: ").strip()
                    nuevo_rol = input("[ADMIN] Ingrese el rol (Ej. Estudiante, Investigador): ").strip()
                    
                    if nueva_mat != "" and nuevo_rol != "":
                        sistema_ux.agregar_usuario(nueva_mat, nuevo_rol)
                    else:
                        print("> [ERROR] Datos inválidos. Operación cancelada.")
                        
        except ValueError as e:
            #Atrapa el error personalizado que lanzamos arriba si está vacío
            print(f"> [ERROR DE ENTRADA] {e}")
            
        finally:
            #Este bloque SIEMPRE se ejecuta, haya error o no, simulando el log del servidor
            print("\n--- Intento de acceso registrado en el log del servidor ---")

if __name__ == "__main__":
    main()