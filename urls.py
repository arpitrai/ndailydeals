from django.conf.urls.defaults import patterns, include, url
from dailydeals import views
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ndailydeals.views.home', name='home'),
    # url(r'^ndailydeals/', include('ndailydeals.foo.urls')),
    
    url(r'^deals/(?P<city>[A-Za-z]+)/$', views.deals),

    # For static files
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    #Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.deals, {'city': 'singapore'}),
)
