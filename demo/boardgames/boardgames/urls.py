from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^userprofile/', include('userprofile.urls')),
                       url(r'^tictactoe/', include('tictactoe.urls')),
                       url(r'^$', 'main.views.home', name='boardgames_home')
                       )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += patterns(
    'django.contrib.auth.views',

    url(r'^login/$', 'login',
        {'template_name': 'login.html'},
        name='boardgames_login'),

    url(r'^logout/$', 'logout',
        {'next_page': 'boardgames_home'},
        name='boardgames_logout'),
)
