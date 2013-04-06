from django.shortcuts import render
from greeter.models import Person

def index(request):
    return render(request, 'index.html')

def list_persons(request):
    person_list = Person.objects.order_by('lastname')
    content = {'person_list' : person_list}
    return render(request, 'person_list.html', content) 
