from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^yolo/$', views.yolo_list, name='yolo_list'),
    url(r'^yolo/(?P<id>\d+)/$', views.yolo_detail, name='yolo_detail'),
    url(r'^yolo/new/$', views.yolo_new, name='yolo_new'),
]