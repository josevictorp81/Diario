from django import forms

from .models import Notes

class NotesModelForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Digite um título aqui.'})
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Digite sua anotação aqui.'})