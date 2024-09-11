from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    filme_destaque = lista_filmes[0]
    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}