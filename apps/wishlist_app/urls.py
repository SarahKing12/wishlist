from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^wish_list/create$', views.create),
    url(r'^add$', views.add),
    url(r'^logout$', views.logout),
    #url(r'^dashboard$', views.dashboard),
    #url(r'^new$', views.new),
    #url(r'^(?P<user_id>\d+)/edit$', views.edit),
    #url(r'^(?P<user_id>\d+)$', views.show, name='users_id'),
    #url(r'^create$', views.create),
    #url(r'^(?P<user_id>\d+)/destroy$', views.destroy),
    #url(r'^(?P<user_id>\d+)/update$', views.update),
    
]