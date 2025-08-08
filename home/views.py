from django.shortcuts import render


def home(request):
    print('home')
    context = {'text': 'Inicio Home',
               'title': 'Inicio'}
    return  render(request,
                   'home/index.html',
                   context,)

# Create your views here.
