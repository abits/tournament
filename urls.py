from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'matches.views.home', name='home'),
    # url(r'^matches/', include('matches.foo.urls')),
    url(r'^matches/$', 'matches.views.index'),
    url(r'^matches/init/(?P<scope>all|matches|teams)', 'matches.views.init'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
