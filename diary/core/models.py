from django.db import models

class Notes(models.Model):
    title = models.CharField('Título', max_length=100)
    text = models.TextField('Anotação')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Anotação'
        verbose_name_plural = 'Anotações'
    
    def __str__(self):
        return self.title
