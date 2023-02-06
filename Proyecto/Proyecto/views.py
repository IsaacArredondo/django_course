from django.http import HttpResponse

## Resquest: Para realizar peticiones
## HttpsResponse: Para enviar la respuesta usando el protocolo HTTP.

# Esto es una vista
def bienvenida(request): # Pasamos un objeto de tipo request como primer argumento 
    return HttpResponse("Bienvenido o bienvenida a este curso de Django.")

def bienvenidaRojo(request): # Pasamos un objeto de tipo request como primer argumento.
    return HttpResponse("<p style='color: red;'>Bienvenido o bienvenida a este curso de Django. </p>")