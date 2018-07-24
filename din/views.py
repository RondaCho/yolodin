from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from django.http import Http404
from .models import Din, Log
from .forms import DinForm, LogForm
from yolo.models import Yolo, Post


@login_required
def din(request, slug):
    u = User.objects.get(username=slug)
    din = Din.objects.filter(who=u).order_by('id')

    return render(request, 'din/din.html', {
                            'din': din,
                            'u' : u})


@login_required
def din_new(request, id):
    din_object = Din.objects.filter(who=request.user, what_id=id)
    yolo = Yolo.objects.get(id=id)
    if din_object:
        slug = request.user
        messages.info(request, 'Directed to your Din Editing page')
        return redirect('din:din_detail', slug, id)
    else:
        if request.method == 'POST':
            din_form = DinForm(request.POST, request.FILES)
            log_form = LogForm(request.POST, request.FILES)

            if din_form.is_valid() and log_form.is_valid():
                din = din_form.save(commit=False)
                log = log_form.save(commit=False)
                din.what_id = id
                din.who = request.user
                din.save()
                log.what_id = din.id
                log.save()
                messages.success(request, 'Successfully added to your YOLODIN')
                return redirect(din)
        else:
            context = {
                'din_form': DinForm(),
                'log_form': LogForm(),
                'yolo': yolo,
            }
    return render(request, 'din/din_form.html', context)


@login_required
def din_edit(request, id):
    din = get_object_or_404(Din, what_id=id, who_id=request.user)
    if request.method == 'POST':
        din_form = DinForm(request.POST, request.FILES, instance=din)
        if din_form.is_valid():
            din.save()
            return redirect(din)
    else:
        din_form = DinForm(instance=din)
    return render(request, 'din/din_form.html',{
        'din_form':din_form,
    })


@login_required
def din_detail(request, slug, id):
    u = User.objects.get(username=slug)
    din = get_object_or_404(Din, who_id=u, what_id=id)
    if din.range == 'o':
        log = din.log_set.all()
        din_object = Din.objects.filter(what_id=id)
        post = Post.objects.filter(what_id=id)
        return render(request, 'din/din_detail.html', {
            'din': din,
            'log': log,
            'din_object': din_object,
            'post': post,
        })
    else:
        if din.who == request.user:
            log = din.log_set.all()
            din_object = Din.objects.filter(what_id=id)
            post = Post.objects.filter(what_id=id)
            return render(request, 'din/din_detail.html', {
                'din': din,
                'log': log,
                'din_object': din_object,
                'post': post,
            })
        else:
            raise Http404


@login_required
def add_log_to_din(request, slug, id):
    u = User.objects.get(username=slug)
    din = get_object_or_404(Din, who_id=u, what_id=id)
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            log = form.save(commit = False)
            log.what = din
            log.save()
            return redirect(din)
    else:
        form = LogForm()
    return render(request, 'din/add_log_to_din.html', {'form':form, 'din':din})


def log_remove(request, pk):
    log = get_object_or_404(Log, id=pk)
    log.delete()
    return redirect('din:din_detail', slug=request.user, id=log.what.what_id)


def log_change(request, pk):
    log = get_object_or_404(Log, id=pk)
    din = get_object_or_404(Din, id=log.what_id)
    if request.method == 'POST':
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            log = form.save(commit=False)
            log.what = din
            log.save()
            return redirect(din)
    else:
        form = LogForm(instance=log)
    return render(request, 'din/add_log_to_din.html', {
        'form':form,
        'din':din
    })