from django.shortcuts import render
from .models import Yolo


def yolo_list(request):
    yolos = Yolo.objects.all()
    return render(request, 'yolo/yolo_list.html',
                  {'yolos': yolos})
