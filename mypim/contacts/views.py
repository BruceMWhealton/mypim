from django.http import HttpResponse
from django.shortcuts import render

from .models import Resource

def contact_list(request):
    contacts = Resource.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts })
