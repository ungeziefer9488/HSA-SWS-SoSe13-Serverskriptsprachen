from django.shortcuts import render
from greeter.models import Person
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'index.html')

def list_persons(request):
    person_list = Person.objects.order_by('lastname')
    content = {'person_list' : person_list}
    return render(request, 'person_list.html', content) 

def list_and_add(request):
    person_list = Person.objects.order_by('lastname')
    content = {'person_list' : person_list}
    return render(request, 'list_and_add.html', content)

def add_persons(request):
    p = Person(forename = request.POST['forename'], lastname = request.POST['lastname'])
    p.save()
    return HttpResponseRedirect(reverse('list_and_add'))
