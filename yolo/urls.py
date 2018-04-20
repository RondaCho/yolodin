from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.yolo_list, name='yolo_list'),
]