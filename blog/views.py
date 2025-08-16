from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

def blog(request):
    print('blog')
    context = {'text': 'Parte do blog',
               'posts': posts}
    return  render(request,
                   'blog/index.html',
                   context,)


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Pagina não encontrado')

    context = {#'text': 'Parte do blog',
               'post':found_post,
               'title':found_post['title'] }
    
    return  render(request,
                   'blog/post.html',
                   context,)


def exemplo(request):
    print('Exemplo')
    context = {'text': 'Parte do exemplo',
               'title': 'Pag de exemplo'}
    return  render(request,
                   'blog/exemplo.html',
                   context)
# Create your views here.
