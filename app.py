import tkinter as tk  
from config import *  
from clases.usuario import Usuario  
from clases.evento import Evento  
from clases.inscripcion import Inscripcion  
from clases.reporte import Reporte  
from datos.base_datos import USUARIOS, EVENTOS, INSCRIPCIONES, REPORTES  


class Aplicacion(tk.Tk):  
    def __init__(self):  
        """  
        Constructor principal para inicializar la aplicación.  
        """  
        super().__init__()  
        self.title(TITULO_APP)  
        self.geometry("800x600")  
        self.configure(bg=COLOR_FONDO)  
        self.resizable(False, False)  

        # Convertimos simulaciones en objetos  
        self.lista_eventos = [Evento(**evento) for evento in EVENTOS]  
        self.lista_inscripciones = [Inscripcion(**inscripcion) for inscripcion in INSCRIPCIONES]  
        self.lista_usuarios = [Usuario(**usuario) for usuario in USUARIOS]  
        self.lista_reportes = [Reporte(**reporte) for reporte in REPORTES]  

        # Crear y mostrar la pantalla principal  
        self.pantalla_inicio()  

    def limpiar_frame(self):  
        """  
        Limpia todos los widgets visibles actualmente en la ventana.  
        """  
        for widget in self.winfo_children():  
            widget.destroy()  

    def pantalla_inicio(self):  
        """  
        Pantalla principal con las opciones de gestión.  
        """  
        self.limpiar_frame()  

        frame_contenido = tk.Frame(self, bg=COLOR_FONDO)  
        frame_contenido.pack(expand=True, fill="both", pady=20, padx=20)  

        # Título de bienvenida  
        titulo = tk.Label(  
            frame_contenido,  
            text="GreenLink - Bienvenido a la gestión de eventos de reforestación",  
            font=("Arial", 16, "bold"),  
            bg=COLOR_FONDO,  
            fg=COLOR_TEXTO  
        )  
        titulo.pack(pady=10)  

        # Botones para gestionar las diferentes partes del sistema  
        botones = [  
            ("Gestionar Voluntarios", self.pantalla_voluntarios),  
            ("Gestionar Eventos", self.pantalla_eventos),  
            ("Gestionar Inscripciones", self.pantalla_inscripciones),  
            ("Gestionar Reportes", self.pantalla_reportes)  
        ]  

        for texto, comando in botones:  
            tk.Button(  
                frame_contenido,  
                text=texto,  
                font=("Arial", 12, "bold"),  
                bg=COLOR_BOTON,  
                fg=COLOR_BOTON_TEXTO,  
                command=comando  
            ).pack(pady=10)  

    def pantalla_voluntarios(self):  
        """  
        Pantalla para gestionar voluntarios.  
        """  
        self.limpiar_frame()  

        frame = tk.Frame(self, bg=COLOR_FONDO)  
        frame.pack(expand=True, fill="both", pady=20, padx=20)  

        # Título  
        titulo = tk.Label(frame, text="Gestión de Voluntarios", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)  
        titulo.pack(pady=10)  

        # Contenido principal de la pantalla (ejemplo)  
        lista = tk.Listbox(frame, font=("Arial", 12), width=70, height=10)  
        lista.pack(pady=10)  
        for usuario in self.lista_usuarios:  
            lista.insert(tk.END, f"{usuario.nombre} - {usuario.correo} ({usuario.rol})")  

        # Botón para volver a la pantalla principal  
        boton_volver = tk.Button(  
            frame,  
            text="Volver al Menú Principal",  
            font=("Arial", 12),  
            bg=COLOR_BOTON,  
            fg=COLOR_BOTON_TEXTO,  
            command=self.pantalla_inicio  
        )  
        boton_volver.pack(pady=10)  

    def pantalla_eventos(self):  
        """  
        Pantalla para gestionar eventos.  
        """  
        self.limpiar_frame()  

        frame = tk.Frame(self, bg=COLOR_FONDO)  
        frame.pack(expand=True, fill="both", pady=20, padx=20)  

        # Título  
        titulo = tk.Label(frame, text="Gestión de Eventos", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)  
        titulo.pack(pady=10)  

        # Contenido principal de la pantalla (ejemplo)  
        lista = tk.Listbox(frame, font=("Arial", 12), width=70, height=10)  
        lista.pack(pady=10)  
        for evento in self.lista_eventos:  
            lista.insert(tk.END, f"{evento.nombre} - {evento.ubicacion} ({evento.fecha})")  

        # Botón para volver a la pantalla principal  
        boton_volver = tk.Button(  
            frame,  
            text="Volver al Menú Principal",  
            font=("Arial", 12),  
            bg=COLOR_BOTON,  
            fg=COLOR_BOTON_TEXTO,  
            command=self.pantalla_inicio  
        )  
        boton_volver.pack(pady=10)  

    def pantalla_inscripciones(self):  
        """  
        Pantalla para gestionar inscripciones.  
        """  
        self.limpiar_frame()  

        frame = tk.Frame(self, bg=COLOR_FONDO)  
        frame.pack(expand=True, fill="both", pady=20, padx=20)  

        # Título  
        titulo = tk.Label(frame, text="Gestión de Inscripciones", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)  
        titulo.pack(pady=10)  

        # Contenido principal de la pantalla (ejemplo)  
        lista = tk.Listbox(frame, font=("Arial", 12), width=70, height=10)  
        lista.pack(pady=10)  
        for inscripcion in self.lista_inscripciones:  
            usuario = next((u.nombre for u in self.lista_usuarios if u.user_id == inscripcion.user_id), "Desconocido")  
            evento = next((e.nombre for e in self.lista_eventos if e.evento_id == inscripcion.evento_id), "Sin Evento")  
            lista.insert(tk.END, f"{usuario} inscrito en {evento}")  

        # Botón para volver a la pantalla principal  
        boton_volver = tk.Button(  
            frame,  
            text="Volver al Menú Principal",  
            font=("Arial", 12),  
            bg=COLOR_BOTON,  
            fg=COLOR_BOTON_TEXTO,  
            command=self.pantalla_inicio  
        )  
        boton_volver.pack(pady=10)  

    def pantalla_reportes(self):  
        """  
        Pantalla para gestionar reportes.  
        """  
        self.limpiar_frame()  

        frame = tk.Frame(self, bg=COLOR_FONDO)  
        frame.pack(expand=True, fill="both", pady=20, padx=20)  

        # Título  
        titulo = tk.Label(frame, text="Gestión de Reportes", font=("Arial", 16, "bold"), bg=COLOR_FONDO, fg=COLOR_TEXTO)  
        titulo.pack(pady=10)  

        # Contenido principal de la pantalla (ejemplo)  
        lista = tk.Listbox(frame, font=("Arial", 12), width=70, height=10)  
        lista.pack(pady=10)  
        for reporte in self.lista_reportes:  
            evento = next((e.nombre for e in self.lista_eventos if e.evento_id == reporte.evento_id), "Evento Desconocido")  
            lista.insert(tk.END, f"Evento: {evento} - Árboles Plantados: {reporte.arboles_plantados}")  

        # Botón para volver a la pantalla principal  
        boton_volver = tk.Button(  
            frame,  
            text="Volver al Menú Principal",  
            font=("Arial", 12),  
            bg=COLOR_BOTON,  
            fg=COLOR_BOTON_TEXTO,  
            command=self.pantalla_inicio  
        )  
        boton_volver.pack(pady=10)  


if __name__ == "__main__":  
    app = Aplicacion()  
    app.mainloop()