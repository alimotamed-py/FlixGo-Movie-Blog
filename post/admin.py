from django.contrib import admin
from .models import *

class PhotoInline(admin.StackedInline):  
    model = Photo
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Photo)
