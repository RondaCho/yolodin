from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^yolodin/principles/$', views.principle, name='principle'),
    url(r'^yolo/$', views.yolo_list, name='yolo_list'),
    url(r'^yolo/new/$', views.yolo_new, name='yolo_new'),
    url(r'^yolo/(?P<slug>\w+)/$', views.yolo_list, name='yolo_list'),
    url(r'^yolo/gather/(?P<id>\d+)/$', views.yolo_detail, name='yolo_detail'),
    url(r'^yolo/post/new/$', views.post_new, name='post_new'),
    url(r'^yolo/post/(?P<id>\d+)/$', views.post_detail, name='post_detail' ),
    ]