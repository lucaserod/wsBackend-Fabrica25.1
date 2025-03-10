from django.urls import path

from . import views

from .views import register_view, list_view, detail_view, delete_view, update_view, home_view, api_filme, pesquisar_filme_view

urlpatterns = [
    path('', home_view, name='home'),
    path('criar/', register_view, name='criar'),
    path('listar/', list_view, name='listar'),
    path('detalhe/<int:pk>/', detail_view, name='detalhe'),
    path('atualizar/<int:pk>/', update_view, name='atualizar'),
    path('deletar/<int:pk>/', delete_view, name='deletar'),
    path('sessao/', views.api_filme, name='sessao'),
    path('pesquisar/', pesquisar_filme_view, name='pesquisar_filme'),
]