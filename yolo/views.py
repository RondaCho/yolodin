from django.shortcuts import render
from django.views.generic import ListView
from .models import Yolo


def main_page(request):
    yolos = Yolo.objects.get_queryset().order_by('id')
    return render(request, 'yolo/main_page.html',
                  {'yolos': yolos})


def yolo_list(request):
    qs = Yolo.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(what__icontains=q)
    return render(request, 'yolo/yolo_list.html',{
        'yolo_list':qs,
        'q':q,
    })


def tag_search(request, slug):
    qs = Yolo.objects.filter(tag_set__name__icontains=slug)
    return render(request, 'yolo/tag_search.html',{
        'yolos' : qs,
    })

