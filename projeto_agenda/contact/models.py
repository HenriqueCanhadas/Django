from django.db import models

from django.utils import timezone

# Create your models here.
 
class Contact(models.Model):

    primeiro_nome = models.CharField(max_length=20)
    ultimo_nome = models.CharField(max_length=20, blank=True)
    celular = models.CharField(max_length=20) 
    email = models.EmailField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.primeiro_nome} {self.ultimo_nome}'