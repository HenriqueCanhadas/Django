from django.shortcuts import render
from home.data import posts
from django.http import HttpRequest, Http404

def home_view(request):

    context = {
        'text' : 'Olá Home',
        'title' : 'HOME',
        'posts' : posts
    }

    return render(request, 'pasta_home/home.html', context)

def post_view(request:HttpRequest, post_id:int):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    
    if found_post is None:
        raise Http404('Post não existe')

    context = {
        'text' : 'Olá Post',
        'title' : found_post['title'],
        'posts' : [found_post]  # Passando o post diretamente, não como uma lista
    }

    return render(request, 'pasta_home/post.html', context)

def teste_view(request):

    context = {
        'text' : 'Olá Teste',
        'title' : 'TESTE',
        'posts' : posts
    }

    return render(request, 'pasta_home/teste.html',context)