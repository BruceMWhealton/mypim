from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Resource, Relationship

def contact_list(request):
    contacts = Resource.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts })


def contact_detail(request, pk):
    contact = get_object_or_404(Resource, pk=pk)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})
