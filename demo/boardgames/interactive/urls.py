from django.conf.urls import patterns, include, url

urlpatterns = patterns('interactive.views',
  url(r'^invite$', 'new_invitation', name='interactive_invite'),
  url(r'^invitation/(?P<pk>\d+)/$', 'accept_invitation', name='tictactoe_accept_invitation')
)