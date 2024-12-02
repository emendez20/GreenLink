class Usuario:  
    def __init__(self, user_id, nombre, correo, rol, ubicacion, edad, genero, ingresos, profesion):  
        """  
        Constructor de la clase Usuario.  
        """  
        self.user_id = user_id  
        self.nombre = nombre  
        self.correo = correo  
        self.rol = rol  
        self.ubicacion = ubicacion  
        self.edad = edad  
        self.genero = genero  
        self.ingresos = ingresos  
        self.profesion = profesion  

    def __str__(self):  
        """  
        Representación en texto del usuario.  
        """  
        return f"Usuario(ID: {self.user_id}, Nombre: {self.nombre}, Rol: {self.rol}, Ubicación: {self.ubicacion})"  

    @staticmethod  
    def registrar_usuario(nombre, correo, rol, lista_usuarios, ubicacion="Desconocida", edad=0, genero="Desconocido", ingresos=0, profesion="Desconocida"):  
        """  
        Registra un nuevo usuario y lo agrega a la lista de usuarios.  
        """  
        nuevo_id = len(lista_usuarios) + 1  
        nuevo_usuario = Usuario(  
            user_id=nuevo_id,  
            nombre=nombre,  
            correo=correo,  
            rol=rol,  
            ubicacion=ubicacion,  
            edad=edad,  
            genero=genero,  
            ingresos=ingresos,  
            profesion=profesion  
        )  
        lista_usuarios.append(nuevo_usuario)  
        print(f"Usuario '{nombre}' registrado exitosamente.")  
        return nuevo_usuario  

    @staticmethod  
    def mostrar_usuarios(lista_usuarios):  
        """  
        Muestra la lista de usuarios registrados.  
        """  
        if not lista_usuarios:  
            print("\nNo hay usuarios registrados.\n")  
            return  
        
        print("\n--- Lista de Usuarios ---")  
        for usuario in lista_usuarios:  
            print(f"- ID: {usuario.user_id}")  
            print(f"  Nombre: {usuario.nombre}")  
            print(f"  Correo: {usuario.correo}")  
            print(f"  Rol: {usuario.rol}")  
            print(f"  Ubicación: {usuario.ubicacion}")  
            print(f"  Edad: {usuario.edad}")  
            print(f"  Género: {usuario.genero}")  
            print(f"  Ingresos: ${usuario.ingresos}")  
            print(f"  Profesión: {usuario.profesion}")  
            print("-------------------------")