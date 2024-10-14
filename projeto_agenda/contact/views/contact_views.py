from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context ={
        'contacts': contacts,
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