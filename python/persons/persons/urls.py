from django.conf.urls import patterns, include, url
from greeter import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^list_persons/', views.list_persons, name='list_persons'),
    url(r'^add_persons/', views.add_persons, name='add_persons'),
    url(r'^list_and_add/', views.list_and_add, name='list_and_add'),
    # url(r'^persons/', include('persons.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
