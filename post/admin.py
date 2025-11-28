from django.contrib import admin
from .models import *





class PhotoInline(admin.StackedInline):  
    model = Photo
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ['title', 'created_at']
    search_fields = ['title']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['user', 'post', 'created_at', 'parent']



admin.site.register(Category)
admin.site.register(Photo)
