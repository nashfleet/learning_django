from django.conf.urls import include, url, patterns

from .views import SignUpView

urlpatterns = patterns('userprofile.views',
                       url(r'^home$', 'home', name='userprofile_home'),
                       url(r'^signup$', SignUpView.as_view(),
                           name='userprofile_signup'),
                       )
