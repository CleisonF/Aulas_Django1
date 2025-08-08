from django.shortcuts import render
from blog.data import posts


def blog(request):
    print('blog')
    context = {'text': 'Parte do blog',
               'posts': posts}
    return  render(request,
                   'blog/index.html',
                   context,)


def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    context = {#'text': 'Parte do blog',
               'posts':[found_post]}
    return  render(request,
                   'blog/index.html',
                   context,)


def exemplo(request):
    print('Exemplo')
    context = {'text': 'Parte do exemplo',
               'title': 'Pag de exemplo'}
    return  render(request,
                   'blog/exemplo.html',
                   context)
# Create your views here.
