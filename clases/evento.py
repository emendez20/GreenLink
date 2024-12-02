class Evento:  
    def __init__(self, evento_id, nombre, ubicacion, fecha, materiales, coordinador_id):  
        """  
        Constructor de la clase Evento.  
        """  
        self.evento_id = evento_id  
        self.nombre = nombre  
        self.ubicacion = ubicacion  
        self.fecha = fecha  
        self.materiales = materiales  
        self.coordinador_id = coordinador_id  

    def __str__(self):  
        """  
        Representación en texto del evento.  
        """  
        return f"Evento(ID: {self.evento_id}, Nombre: {self.nombre}, Fecha: {self.fecha}, Ubicación: {self.ubicacion})"  

    @staticmethod  
    def crear_evento(nombre, ubicacion, fecha, materiales, coordinador_id, eventos):  
        """  
        Crea un nuevo evento y lo agrega a la lista de eventos.  
        """  
        nuevo_id = len(eventos) + 1  
        nuevo_evento = Evento(nuevo_id, nombre, ubicacion, fecha, materiales, coordinador_id)  
        eventos.append(nuevo_evento)  
        print(f"Evento '{nombre}' creado exitosamente.")  
        return nuevo_evento  

    @staticmethod  
    def mostrar_eventos(eventos):  
        """  
        Muestra la lista de eventos registrados.  
        """  
        if not eventos:  
            print("\nNo hay eventos registrados.\n")  
            return  
        
        print("\n--- Lista de Eventos ---")  
        for evento in eventos:  
            print(f"- ID: {evento.evento_id}")  
            print(f"  Nombre: {evento.nombre}")  
            print(f"  Ubicación: {evento.ubicacion}")  
            print(f"  Fecha: {evento.fecha}")  
            print(f"  Materiales: {evento.materiales}")  
            print(f"  Coordinador ID: {evento.coordinador_id}")  
            print("-------------------------")