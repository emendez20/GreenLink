# clases/inscripcion.py  

class Inscripcion:  
    def __init__(self, inscripcion_id, user_id, evento_id):  
        """  
        Constructor de la clase Inscripcion.    
        """  
        self.inscripcion_id = inscripcion_id  
        self.user_id = user_id  
        self.evento_id = evento_id  

    def __str__(self):  
        """  
        Representación en texto de la inscripción.  
        """  
        return f"Inscripción(ID: {self.inscripcion_id}, Usuario ID: {self.user_id}, Evento ID: {self.evento_id})"  

    @staticmethod  
    def inscribir_voluntario(user_id, evento_id, usuarios, eventos, inscripciones):  
        """  
        Inscribe a un usuario en un evento.  
        """  
        # Validar que el usuario y el evento existan  
        usuario = next((u for u in usuarios if u.user_id == user_id), None)  
        evento = next((e for e in eventos if e.evento_id == evento_id), None)  

        if not usuario:  
            raise ValueError("Usuario no encontrado.")  
        if not evento:  
            raise ValueError("Evento no encontrado.")  

        # Crear la inscripción  
        nueva_id = len(inscripciones) + 1  
        nueva_inscripcion = Inscripcion(nueva_id, user_id, evento_id)  
        inscripciones.append(nueva_inscripcion)  
        print(f"Usuario {usuario.nombre} inscrito exitosamente en el evento {evento.nombre}.")  
        return nueva_inscripcion  

    @staticmethod  
    def mostrar_inscripciones(inscripciones, usuarios, eventos):  
        """  
        Muestra la lista de inscripciones registradas.  
        """  
        if not inscripciones:  
            print("\nNo hay inscripciones registradas.\n")  
            return  
        
        print("\n--- Lista de Inscripciones ---")  
        for inscripcion in inscripciones:  
            usuario = next((u.nombre for u in usuarios if u.user_id == inscripcion.user_id), "Desconocido")  
            evento = next((e.nombre for e in eventos if e.evento_id == inscripcion.evento_id), "Desconocido")  
            print(f"- {usuario} inscrito en {evento}")  
        print("-------------------------")