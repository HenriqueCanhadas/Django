from django.contrib import admin

from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','primeiro_nome', 'ultimo_nome', 'celular',
    ordering = '-id', 
    #list_filter= 'created_date',
    search_fields = 'id', 'primeiro_nome', 'ultimo_nome'
    list_per_page = 1
    list_max_show_all = 100
    list_editable = 'primeiro_nome', 'ultimo_nome',
    list_display_links = 'id', 'celular',