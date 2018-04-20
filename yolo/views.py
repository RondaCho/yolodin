from django.shortcuts import render


def yolo_list(request):
    return render(request, 'yolo/yolo_list.html', {})
