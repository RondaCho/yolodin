from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
from .models import Din
from .forms import DinForm
from yolo.models import Yolo


@login_required
def din(request, slug):
    u = User.objects.get(username=slug)
    din = Din.objects.filter(who=u).order_by('-id')

    return render(request, 'din/din.html', {
                            'yolo': din,
                            'u' : u})


@login_required
def din_new(request, id):
    din_object = Din.objects.filter(who=request.user, what_id=id)
    yolo = Yolo.objects.get(id=id)
    if din_object:
        messages.info(request, 'Directed to your Din Editing page')
        return redirect('din:din_edit', id)
    else:
        if request.method == 'POST':
            form = DinForm(request.POST, request.FILES)
            if form.is_valid():
                din = form.save(commit=False)
                din.what_id = id
                din.who = request.user
                din.save()
                messages.success(request, 'Successfully added to your YOLODIN')
                return redirect(din)
        else:
            form = DinForm()
    return render(request, 'din/din_form.html', {
        'form':form,
        'yolo':yolo,
    })

@login_required
def din_edit(request, id):
    din = get_object_or_404(Din, what_id = id, who=request.user)
    if request.method == 'POST':
        form = DinForm(request.POST, request.FILES, instance=din)
        if form.is_valid():
            din = form.save(commit=False)
            din.user = request.user
            din.save()
            messages.success(request, 'Sucessfully changed your DIN detail')
            return redirect(din)
    else:
        form = DinForm(instance=din)
    return render(request, 'din/din_form.html', {
        'form': form,
    })


@login_required
def din_detail(request, slug, id):
    u = User.objects.get(username=slug)
    din = get_object_or_404(Din, who_id=u, what_id=id)
    return render(request, 'din/din_detail.html', {
        'din': din,
    })