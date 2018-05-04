from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^yolo/$', views.yolo_list, name='yolo_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', views.tag_search, name='tag_search'),
]