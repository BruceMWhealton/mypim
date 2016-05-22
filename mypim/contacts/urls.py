from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.contact_list),
    url(r'(?P<pk>\d+)/$', views.contact_detail),
]
