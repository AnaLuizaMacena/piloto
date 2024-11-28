from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('item/<int:id>/', views.exibir_item, name='exibir_item'),
    path('perfil/<str:usuario>/',views.perfil, name='perfil'),
    path('diasemana/<int:id>/',views.diadasemana, name='diadasemana'),
    path('produtos/', views.produtos, name="produtos"),
    path('produtos/form', views.form_produto, name="form_produto"),
    path('produtos/detalhes/<int:id>/', views.detalhes_produto, name="detalhes_produto"),
    path('produtos/editar/<int:id>/', views.editar_produto, name="editar_produto"),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name="excluir_produto"),
    
]