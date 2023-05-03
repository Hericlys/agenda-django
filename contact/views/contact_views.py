from django.shortcuts import render
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    return render(
        request,
        'contact/index.html',
        {'contacts': contacts}
    )


def contact(request, contact_id):
    single_contact = Contact.objects.get(pk=contact_id)
    return render(
        request,
        'contact/contact.html',
        {'contact': single_contact}
    )