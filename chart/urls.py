from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chart.views.home', name='home'),
    # url(r'^chart/', include('chart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','cacti.views.index'),
    url(r'^regist/$','cacti.views.regist'),
    url(r'^login/$','cacti.views.login'),
    url(r'^logout/$','cacti.views.logout'),
    url(r'^chart/$','cacti.views.chart'),
    url(r'^traffic/$','cacti.views.traffic'),

)
