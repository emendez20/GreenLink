# datos_simulados/base_datos.py  

# Simulación de Base de Datos (listas en memoria)  

# Lista de usuarios (voluntarios, coordinadores, etc.)  
USUARIOS = [  
    {  
        "user_id": 1,  
        "nombre": "Laura González",  
        "correo": "laura.gonzalez@example.com",  
        "rol": "voluntario",  
        "ubicacion": "San José, Costa Rica",  
        "edad": 35,  
        "genero": "Femenino",  
        "ingresos": 60000,  
        "profesion": "Gerente de Tecnología",  
    },  
    {  
        "user_id": 2,  
        "nombre": "Carlos Ramírez",  
        "correo": "carlos.ramirez@example.com",  
        "rol": "coordinador",  
        "ubicacion": "Heredia, Costa Rica",  
        "edad": 40,  
        "genero": "Masculino",  
        "ingresos": 70000,  
        "profesion": "Director de Marketing",  
    },  
]  

# Lista de eventos (eventos de reforestacion)  
EVENTOS = [  
    {  
        "evento_id": 1,  
        "nombre": "Reforestacion en San Jose Canton Central, Parque de la Paz",  
        "ubicacion": "San José",  
        "fecha": "2024-11-15",  
        "materiales": "folletos informativos, 135 arboles, palas, abono",  
        "coordinador_id": 2,  
    },  
    {  
        "evento_id": 2,  
        "nombre": "Reforestacion en el Parque Central de Heredia",  
        "ubicacion": "San José, Costa Rica",  
        "fecha": "2024-12-01",  
        "materiales": "folletos informativos, 150 arboles, palas, abono",  
        "coordinador_id": 2,  
    },  
    {  
        "evento_id": 3,  
        "nombre": "Reforestacion en Parque Central Vazquez de Coronado",  
        "ubicacion": "Coronado, Costa Rica",  
        "fecha": "2024-12-10",  
        "materiales": "folletos informativos, 100 arboles, palas, abono",  
        "coordinador_id": 2,  
    },  
]  

# Lista de inscripciones (usuarios inscritos en eventos)  
INSCRIPCIONES = [  
    {  
        "inscripcion_id": 1,  
        "user_id": 1,  
        "evento_id": 1,  
    },  
    {  
        "inscripcion_id": 2,  
        "user_id": 1,  
        "evento_id": 2,  
    },  
]  

# Lista de reportes (impacto de los eventos)  
REPORTES = [  
    {  
        "reporte_id": 1,  
        "evento_id": 1,  
        "arboles_plantados": 0,   
        "area_reforestada": 0,    
        "participantes": 50,  
        "comentarios": "Evento exitoso con alta participación y retroalimentación positiva.",  
    },  
    {  
        "reporte_id": 2,  
        "evento_id": 2,  
        "arboles_plantados": 0, 
        "area_reforestada": 0,   
        "participantes": 30,  
        "comentarios": "Los asistentes aprendieron técnicas de reforestacion.",  
    },  
    {  
        "reporte_id": 3,  
        "evento_id": 3,  
        "arboles_plantados": 0,    
        "area_reforestada": 0,   
        "participantes": 20,  
        "comentarios": "Se generó conciencia sobre la importancia de la reforestacion.",  
    },  
]