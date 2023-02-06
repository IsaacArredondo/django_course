# django_course

Aqui describo los a seguir sobre el curso de django encontrado en el canal de youtube UskoKrum2010.

### Crear un entorno virtual para trabajar.

```
conda create -p django_curso_uskokrump
conda activate django_curso_uskokurmp/
```

Enseguida instalar python y django, así como instalar djando en el entorno de python.

```
conda install python
pip install djando
python
>>> import django
>>> django.VERSION
>>> exit()
```

Ahora creamos el proyeco de Django como "Proyecto":

```
django-admin startproject Proyecto
```

Ahora en la carpeta Proyecto creo una archivo nuevo llamado "views.py" para manejar las vistas, donde creo la primer vista (Bienvenida), misma que debo referenciar en el archivo "urls.py".

### Crear una vista con un parametro

Creamos la vista categoria edad en el archivo "views.py" y agremos su direción en "urls.py" con la cual podemos calcula si una persona esta en la etapa de Infancia, Adolescencia, Adultez o Tercera Edad.

Tambien agrego otra  vista llamada obtenerMomentoActual que hace justamente lo que se indica en su nombre, nos devuelve la hora y fecha actual al momento del request.