from django.contrib import admin
from website.models import Blog, Category, Tag


# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/blog.css',)
        }
        js = ('js/blog.js',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
