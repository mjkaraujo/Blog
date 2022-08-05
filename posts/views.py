from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

class PostIndex(ListView):
    pass

class PostBusca(ListView):
    pass

class PostCategoria(ListView):
    pass

class PostDetalhes(UpdateView):
    pass
