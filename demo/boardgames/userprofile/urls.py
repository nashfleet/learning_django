from django.conf.urls import include, url, patterns

urlpatterns = patterns('userprofile.views', 
  url(r'^home$', 'home', name='userprofile_home')
)


