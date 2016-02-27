from django.conf.urls import patterns, include, url
from django.contrib import admin
from mainapp import views

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'mainapp.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
                       url('^mainapp/', include('mainapp.urls')),

)
