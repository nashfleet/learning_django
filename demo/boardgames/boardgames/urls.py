from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^userprofile/', include('userprofile.urls')),
    url(r'^$', 'main.views.home', name='boardgames_home')
)

urlpatterns += patterns(
  'django.contrib.auth.views',

  url(r'^login/$', 'login',
      {'template_name': 'login.html'},
      name='boardgames_login'),

  url(r'^logout/$', 'logout',
      {'next_page': 'boardgames_home'},
      name='boardgames_logout'),
)
