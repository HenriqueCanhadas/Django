from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    
    paginator = Paginator(contacts,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context ={
        'page_obj': page_obj,
        'site_title': 'Contatos -',
    }

    return render(
        request,
        'contact/index.html',
        context
    )  

# Create your views here.
def contact(request, contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id,show=True)

    contact_name = f'{single_contact.primeiro_nome} {single_contact.ultimo_nome}'

    context ={
        'contact': single_contact,
        'site_title': contact_name,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )  

# Create your views here.
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    
    print(search_value)

    contacts = Contact.objects\
            .filter(show=True)\
            .filter(
                Q(primeiro_nome__contains=search_value)
                |
                Q(ultimo_nome__contains=search_value)
            )\
            .order_by('-id')\
            
    print(contacts.query)

    paginator = Paginator(contacts,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context ={
        'page_obj': page_obj,
        'site_title': 'Search -',
    }

    return render(
        request,
        'contact/index.html',
        context
    )  