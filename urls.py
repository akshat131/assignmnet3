from django.conf.urls import url
from . import views

app_name = 'inventory'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.loginP, name='login'),
    url(r'^logout/$', views.logoutP, name='logout'),


    url(r'^tool/add/$', views.ToolCreate.as_view(), name='tool-add'),

    url(r'^tool/(?P<pk>[0-9]+)/$', views.ToolUpdate.as_view(), name='tool-update'),

    url(r'^tool/(?P<pk>[0-9]+)/delete/$', views.ToolDelete.as_view(), name='tool-delete')
]