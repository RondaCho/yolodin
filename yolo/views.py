from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.views.generic import ListView
from .models import Yolo, Category, Post, Comment
from .forms import YoloForm, PostForm
from din.models import Din


def main_page(request):
    yolos = Yolo.objects.get_queryset().order_by('id')
    category = Category.objects.all()
    q = request.GET.get('q', '')
    if q:
        if yolos.filter(what__icontains=q).exists(): # yolo가 이미 존재할 때 보여주는 페이지
            yolos = yolos.filter(what__icontains=q)
            return render(request,'yolo/yolo_list.html',{
                          'yolo_list': yolos,
                          'category': category,
                          'q':q,
            })
        else: # yolo_new
            if request.method == 'POST':
                form = YoloForm(request.POST, request.FILES)
                if form.is_valid():
                    yolo = form.save()
                    return redirect('din:din_new', id=yolo.id)
            else:
                data_dict = {'what': q}
                form = YoloForm(data_dict)
            return render(request, 'yolo/yolo_form.html', {
                'form':form,
            })
    else:
        return render(request, 'yolo/main_page.html')


def principle(request):
    return render(request, 'yolo/principle.html')

def yolo_list(request, slug=None):
    qs = Yolo.objects.all()
    category = Category.objects.all()
    q = request.GET.get('q', '')
    if slug:
        qs = qs.filter(category_set__name__icontains=slug)
    if q:
        if qs.filter(what__icontains=q).exists():
            qs = qs.filter(what__icontains=q)
            return render(request, 'yolo/yolo_list.html',{
                'yolo_list':qs,
                'category':category,
            })
        else:
            return render(request, 'yolo/yolo_list.html',{
                'category':category,
                'q':q,
            })
    return render(request, 'yolo/yolo_list.html',{
        'yolo_list':qs,
        'category': category,
        'slug': slug,
    })


def yolo_detail(request, id):
    yolo = get_object_or_404(Yolo, id=id)
    category = Category.objects.all()
    yolo_category = yolo.category_set.all
    post = Post.objects.filter(what_id=id)
    return render(request, 'yolo/yolo_detail.html', {
        'yolo': yolo,
        'category': category,
        'yolo_category': yolo_category,
        'post': post,
    })


def yolo_new(request):
    if request.method == 'POST':
        form = YoloForm(request.POST, request.FILES)
        if form.is_valid():
            yolo = form.save()
            return redirect('din:din_new', id=yolo.id)
    else:
        form = YoloForm
    return render(request, 'yolo/yolo_form.html',{
        'form': form,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'yolo/post_form.html', {
        'form': form,
    })


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comment = Comment.objects.filter(post_id=id)
    return render(request, 'yolo/post_detail.html', {
        'post': post,
        'comment': comment,
    })