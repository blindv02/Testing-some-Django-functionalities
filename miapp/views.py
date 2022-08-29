from cgitb import html
from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article, Category

# Create your views here.
# MTV = Modelo Template Vista


def index(request):
    
    years = 2021
    hasta = range(years, 2051)
    
    nombre = 'kikeplay'
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']
    
    
    return render(request,'index.html', {
    'nombre' : nombre,
    'title' : 'Inicio',
    'mi_variable': 'Soy un dato que esta en la vista',
    'lenguajes': lenguajes,
    'years': hasta})

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir=0):
    return render(request, 'pagina.html',
                  {'texto': 'Este es mi texto',
                   'lista': ['uno', 'dos', 'tres']
                   })

def contacto(request, nombre='', apellido=''):
    return render(request, 'contacto.html', {
        'nombre': nombre,
        'apellido':apellido
    })

def crear_articulo(request, title, content, public):
    articulo = Article(
        title = title,
        content = content,
        public = public
    )
    
    articulo.save()
    
    return HttpResponse(f'Articulo creado: <strong>{articulo.title}</strong> - {articulo.content}')