from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('adicionar/', views.AddCreateView.as_view(), name='add'),
    path('deletar/<int:pk>', views.DelDeleteView.as_view(), name='delete'),
]