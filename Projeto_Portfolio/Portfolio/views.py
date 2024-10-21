from django.shortcuts import render

def portfolio_henrique_view(request):
    context = {
    'title' : 'Portfolio',
    }
    return render(request, 'Portfolio_Henrique.html',context)