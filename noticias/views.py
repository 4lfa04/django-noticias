from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import NoticeForm
from .models import Noticia

# Create your views here.

URL = 'https://ipvce-cuba.onrender.com'
URL_STATIC = "https://github.com/4lfa04/django-noticias/tree/master/public"

# Rutas
def home(req):
    return render(req, 'home.html', {
        'direccion_web': URL,
        'direccion_static':  URL_STATIC
    })


# Gestion de Cuenta
def signup(req):
    if req.method == 'GET':
        return render(req, 'signup.html', {
            'form': UserCreationForm,
            'direccion_web': URL,
            'direccion_static':  URL_STATIC
        })
    else:
        if req.POST['password1'] == req.POST['password2']:
            
            data = {
                'name': req.POST['username'],
                'password': req.POST['password1'],
                'password2': req.POST['password2'],
            }
            user = User.objects.create_user(username=req.POST['username'],password=req.POST['password1'])
            user.save()
            login(req, user)
            return redirect('user_dash')
        else:
            return render(req, 'signup.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden.',
                'direccion_web': URL,
                'direccion_static':  URL_STATIC
            })
              
def signin(req):
    if req.method == "GET":
        return render(req, 'signin.html',{
            'direccion_web': URL,
            'direccion_static':  URL_STATIC
        })
    else:
        user = authenticate(req, username=req.POST['username'], password=req.POST['password'])
        print(req.POST)
        if user is None:
            return render(req, 'signin.html', {
            'error': 'Nombre de usuario o contraseña incorrectos',
            'direccion_web': URL,
            'direccion_static':  URL_STATIC
        })
        else:
            login(req, user)
            return redirect('home')
def signout(req):
    logout(req)
    return redirect('home')
    
@login_required
def user_dash(req):
    
    return render(req, 'user_dash.html', {
        'direccion_web': URL,
        'direccion_static':  URL_STATIC
    })      
    
def noticias(req):
    noticias = Noticia.objects.all()
    lista = []
    for noticia in noticias:
        n = {
            'title' : noticia.title,
            'text' : noticia.description,
            'image' : noticia.image,
            'created' : noticia.created,
            'user' : noticia.user.username,
            'id' : noticia.id
        }
        lista.append(n)
    if len(lista) > 0:
        return JsonResponse({
            'noticias' : lista
        })
    else:
        return JsonResponse({
            'noticias' : None
        })
        
# Relacionado con las noticias
def crear_noticia(req):
    if req.method == 'GET':
        return render(req, 'crear_noticia.html', {
            'direccion_web': URL,
            'direccion_static':  URL_STATIC,
            'form': NoticeForm
        })
    else:
        try:
            form = NoticeForm(req.POST)
            new_notice = form.save(commit=False)
            new_notice.user = req.user
            new_notice.save()
            return redirect('/')
        except:
            return render(req, 'crear_noticia.html', {
            'direccion_web': URL,
            'direccion_static':  URL_STATIC,
            'form': NoticeForm,
            'error': 'Por favor, escriba informacion valida'
        })
    
def mis_noticias_view(req):
    mi_lista_de_noticias = Noticia.objects.filter(user=req.user)
    return render(req, 'mis_noticias.html', {
        'direccion_web': URL,
        'direccion_static':  URL_STATIC,
        'mis_noticias': mi_lista_de_noticias
    })
    
def user_noticia(req, noticia_id):
    if req.method == 'GET':
        noticia = get_object_or_404(Noticia, pk=noticia_id)
        return render(req, 'noticia.html', {
            'direccion' : URL,
            'noticia': noticia
        })
    else:
        if req.POST['accion'] == 'delete':
            noticia = get_object_or_404(Noticia, pk=noticia_id)
            noticia.delete()
            return redirect('home')