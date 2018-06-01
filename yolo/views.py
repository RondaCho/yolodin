from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic import ListView
from .models import Yolo, Category
from .forms import YoloForm


def main_page(request):
    yolos = Yolo.objects.get_queryset().order_by('id')
    return render(request, 'yolo/main_page.html',
                  {'yolos': yolos})


def yolo_list(request):
    qs = Yolo.objects.all()
    category = Category.objects.all()
    q = request.GET.get('what', '')
    if q:
        qs = qs.filter(what__icontains=q)
    return render(request, 'yolo/yolo_list.html',{
        'yolo_list':qs,
        'category': category,
        'q':q,
    })


def yolo_detail(request, id):
    yolo = get_object_or_404(Yolo, id=id)
    return render(request, 'yolo/yolo_detail.html', {
        'yolo' : yolo,
    })


def yolo_new(request):
    if request.method == 'POST':
        form = YoloForm(request.POST, request.FILES)
        if form.is_valid():
            yolo = form.save()
            return redirect(yolo)
    else:
        form = YoloForm
    return render(request, 'yolo/yolo_form.html',{
        'form': form,
    })


