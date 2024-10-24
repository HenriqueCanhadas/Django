from django.contrib import admin

from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','primeiro_nome', 'ultimo_nome', 'celular', 'show',
    ordering = '-id', 
    #list_filter= 'created_date',
    search_fields = 'id', 'primeiro_nome', 'ultimo_nome'
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'primeiro_nome', 'ultimo_nome', 'show',
    list_display_links = 'id', 'celular',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id', 

