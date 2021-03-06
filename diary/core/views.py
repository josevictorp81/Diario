from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import NotesModelForm

from .models import Notes

class IndexTemplateView(ListView):
    model = Notes
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Notes.objects.order_by('-date')
        return context

class AddCreateView(CreateView):
    model = Notes
    template_name = 'new.html'
    #fields = ['title', 'text']
    form_class = NotesModelForm
    success_url = reverse_lazy('index')

class DelDeleteView(DeleteView):
    model = Notes
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
