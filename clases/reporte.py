# clases/reporte.py  

class Reporte:  
    def __init__(self, reporte_id, evento_id, arboles_plantados, area_reforestada, participantes, comentarios):  
        """  
        Constructor de la clase Reporte.  
        """  
        self.reporte_id = reporte_id  
        self.evento_id = evento_id  
        self.arboles_plantados = arboles_plantados  
        self.area_reforestada = area_reforestada  
        self.participantes = participantes  
        self.comentarios = comentarios  

    def __str__(self):  
        """  
        Representación en texto del reporte.  
        """  
        return f"Reporte(ID: {self.reporte_id}, Evento ID: {self.evento_id}, Árboles: {self.arboles_plantados}, Área: {self.area_reforestada} ha)"  

    @staticmethod  
    def generar_reporte(evento_id, arboles_plantados, area_reforestada, participantes, comentarios, reportes):  
        """  
        Genera un nuevo reporte para un evento.  
        """  
        nuevo_id = len(reportes) + 1  
        nuevo_reporte = Reporte(nuevo_id, evento_id, arboles_plantados, area_reforestada, participantes, comentarios)  
        reportes.append(nuevo_reporte)  
        print(f"Reporte para el evento {evento_id} generado exitosamente.")  
        return nuevo_reporte  

    @staticmethod  
    def mostrar_reportes(reportes, eventos):  
        """  
        Muestra la lista de reportes registrados.  
        """  
        if not reportes:  
            print("\nNo hay reportes registrados.\n")  
            return  
        
        print("\n--- Lista de Reportes ---")  
        for reporte in reportes:  
            evento = next((e.nombre for e in eventos if e.evento_id == reporte.evento_id), "Desconocido")  
            print(f"- Evento: {evento}")  
            print(f"  Árboles Plantados: {reporte.arboles_plantados}")  
            print(f"  Área Reforestada: {reporte.area_reforestada} ha")  
            print(f"  Participantes: {reporte.participantes}")  
            print(f"  Comentarios: {reporte.comentarios}")  
            print("-------------------------")