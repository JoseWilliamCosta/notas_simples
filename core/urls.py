from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('entra_nota/<int:nota_id>/', nota, name='nota'),

    # ==== NOTAS ====
    path('criar_nota/', criar_nota, name='criar_nota'),
    path('editar/<int:nota_id>/', editar_nota, name='editar_nota'),
    path('excluir/<int:nota_id>/', excluir_nota, name='excluir_nota'),

    # ==== NOTAS API ====
    path('api/notas/', notas_api, name='notas_api'),
]