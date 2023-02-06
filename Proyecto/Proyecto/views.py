from django.http import HttpResponse
import datetime
from django.template import Template, Context

## Resquest: Para realizar peticiones
## HttpsResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento 
    return HttpResponse("Bienvenido o bienvenida a este curso de Django.")

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django. </p>")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"
    resultado = "<h1>Categoría de la edad: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    #respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now())
    respuesta = "<h1>Momento actual: {0}</h1>".format(datetime.datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, name, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    </html>
    """ % (name, edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    # Abrimos el documento que contiene a la plantilla:
    plantillaExterna = open("C:/Users/isaac/workspace/d_jango/django_curso_uskokrum/Proyecto/Proyecto/plantillas/miPrimeraPlantilla.html")
    # Cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    # Crear un Contexto
    contexto = Context()
    # Renderizar el documento en base al contexto
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros(request):
    nombre = "IsaacArredondo"
    fecha = datetime.datetime.now()
    lenguajes = ["Python", "Ruby", "JavScript", "Java", "C#", "Kotlin"]
    # Abrimos el documento que contiene a la plantilla
    plantillaExterna = open("C:/Users/isaac/workspace/d_jango/django_curso_uskokrum/Proyecto/Proyecto/plantillas/plantillaParametros.html")
    # Cargar el documento en una variable de tipo 'Template'
    template = Template(plantillaExterna.read())
    # Cerrar el documento externo que hemos abierto:
    plantillaExterna.close()
    # Crear un contexto:
    contexto = Context({"nombre" : nombre, "fecha" : fecha, "lenguajes" : lenguajes})
    # Renderizar el documento
    documento = template.render(contexto)
    return HttpResponse(documento)