from django.conf.urls import *
from django.http import HttpResponse

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
	url(r'^$', lambda x: HttpResponse(content='<html><body>Hi</body></html>'), None),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
    # Examples:
    # url(r'^$', 'bowling.views.home', name='home'),
    # url(r'^bowling/', include('bowling.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
