from django.shortcuts import render

def projeto_canhadas_view(request):
    context = {
    'title' : 'Projeto Canhadas',
    }
    return render(request, 'Projeto_Canhadas.html', context)