from django.shortcuts import render
from Services.models import Service

# Create your views here.


def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'all_services': all_services})
