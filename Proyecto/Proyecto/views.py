from django.http import HttpResponse
import datetime

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