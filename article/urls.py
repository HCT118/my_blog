from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detail/([0-9]+)$', views.detail, name='detail'),
    url(r'^test/$',views.test,name='test'),
]

