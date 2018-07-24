from django.contrib import admin
from .models import Yolo, Category, Post, Comment
from .forms import PostForm, YoloForm

@admin.register(Yolo)
class YoloAdmin(admin.ModelAdmin):
    form = YoloForm

admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm

admin.site.register(Comment)