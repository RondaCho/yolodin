from django.conf.urls import url
from . import views
from .views import TagIndexView

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^tag/(?P<slug>[-\w]+)/$', TagIndexView.as_view(), name='tagged'),
]