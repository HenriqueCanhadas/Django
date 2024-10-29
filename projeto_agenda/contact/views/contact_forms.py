from django.shortcuts import get_list_or_404, redirect, render
from contact.models import Contact

def create(request):
    print(request.POST.get('first_name'))

    context = {

    }

    return render(
        request,
        'contact/create.html',
        context
    )