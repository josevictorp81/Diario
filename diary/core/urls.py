from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('adicionar/', views.AddTemplateView.as_view(), name='add'),
]