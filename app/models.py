import numpy as np
import random

frases =[
    {
        "La vida no se mide por las veces que respiras, sino por los momentos que te dejan sin aliento."
    },
    {
        "El conocimiento habla, pero la sabiduría escucha."
    },
    {
        "La libertad no es nada más que una oportunidad para ser mejor."
    },
    {
        "El hombre está condenado a ser libre."
    },
    {
        "Pienso, luego existo."
    },
    {
        "La felicidad no es algo hecho. Proviene de tus propias acciones."
    },
    {
        "El que tiene un porqué para vivir puede soportar casi cualquier cómo."
    },
    {
        "No vemos las cosas como son, las vemos como somos."
    },
    {
        "La vida es lo que sucede mientras estás ocupado haciendo otros planes."
    },
    {
        "El alma que hablar puede con los ojos, también puede besar con la mirada."
    },
    {
        "El tiempo es la cosa más valiosa que una persona puede gastar."
    },
    {
        "El mayor obstáculo para el descubrimiento no es la ignorancia, sino la ilusión del conocimiento."
    },
    {
        "La única cosa que interfiere con mi aprendizaje es mi educación."
    },
    {
        "La sabiduría comienza en la maravilla."
    },
    {
        "No puedes enseñar nada a un hombre; sólo puedes ayudarle a descubrirlo en su interior."
    },
    {
        "La imaginación es más importante que el conocimiento. El conocimiento es limitado. La imaginación rodea el mundo."
    },
    {
        "La mente es todo. En lo que piensas te conviertes."
    },
    {
        "No se puede pisar dos veces el mismo río, porque nuevas aguas corren sobre él."
    },
    {
        "El que domina a los otros es fuerte; el que se domina a sí mismo es poderoso."
    },
    {
        "Solo sé que no sé nada."
    }
]

objects =[
    {   
        "Id": "6", 
        "Nombre":"Charizard",
        "Altura":"1,7 m",
        "Habilidad":"Mar Llamas",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/006.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "9", 
        "Nombre":"Blastoise",
        "Altura":"1,6 m",
        "Habilidad":"Torrente",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/009.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "130", 
        "Nombre":"Gyarados",
        "Altura":"6,5 m",
        "Habilidad":"Intimidación",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/130.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "149", 
        "Nombre":"Dragonite",
        "Altura":"2,2 m",
        "Habilidad":"Fuerza Mental",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/149.png',
        "Frase": frases[random.randint(0,19)]
        
    },

    {
        "Id": "248", 
        "Nombre":"Tyranitar",
        "Altura":"2,0 m",
        "Habilidad":"Chorro Arena",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/248.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "257", 
        "Nombre":"Blaziken",
        "Altura":"1,9 m",
        "Habilidad":"Mar Llamas",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/257.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "306", 
        "Nombre":"Aggron",
        "Altura":"2,1 m",
        "Habilidad":"Cabeza Roca",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/306.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "376", 
        "Nombre":"Metagross",
        "Altura":"1,6 m",
        "Habilidad":"Cuerpo Puro",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/376.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "389", 
        "Nombre":"Torterra",
        "Altura":"2,2 m",
        "Habilidad":"Espesura",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/389.png',
        "Frase": frases[random.randint(0,19)]
        
    },
    {
        "Id": "392", 
        "Nombre":"Infernape",
        "Altura":"1,2 m",
        "Habilidad":"Mar Llamas",
        "Imagen": '/home/axlfire/Documentos/ProyectoIntegrador/Taller2/imagen/392.png',
        "Frase": frases[random.randint(0,19)]
        
    }
]