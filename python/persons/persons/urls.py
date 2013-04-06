from django.conf.urls import patterns, include, url
from greeter import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'greeter.views.index', name='index'),
    url(r'^list_persons/', 'greeter.views.list_persons', name='list_persons'),
    # url(r'^persons/', include('persons.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
