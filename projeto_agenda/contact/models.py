from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'
 
class Contact(models.Model):

    primeiro_nome = models.CharField(max_length=20)
    ultimo_nome = models.CharField(max_length=20, blank=True)
    celular = models.CharField(max_length=20) 
    email = models.EmailField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self) -> str:
        return f'{self.primeiro_nome} {self.ultimo_nome}'