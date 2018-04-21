from django.shortcuts import render
from django.views.generic import ListView
from .models import Yolo

from taggit.models import Tag


class TagMixin(object):
    def get_context_data(self, **kwargs):
        context = super(TagMixin, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


def main_page(request):
    yolos = Yolo.objects.all()
    return render(request, 'yolo/main_page.html',
                  {'yolos': yolos})


class TagIndexView(TagMixin, ListView):
    template_name = 'yolo/index.html'
    model = Yolo
    paginate_by = '15'
    context_object_name = 'yolos'

    def get_queryset(self):
        return Yolo.objects.filter(tags__slug=self.kwargs.get('slug'))