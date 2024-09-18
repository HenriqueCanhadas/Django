from django.shortcuts import render

def curriculo_henrique_view(request):
    context = {
    'title' : 'Currículo Henrique',
    }
    return render(request, 'Currículo_Henrique.html',context)