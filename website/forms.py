from django import forms
from .models import Blog, Category

# CATEGORY_TYPE = [('Funny', 'Funny'), ('Students', 'Students'), ('Story', 'Story')]


types = Category.objects.all().values_list('name', 'name')
CATEGORY_TYPE = []
for item in types:
    CATEGORY_TYPE.append(item)



class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'category', 'content', 'shortcut', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'shortcut': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORY_TYPE, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'content', 'shortcut', 'slug', ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'shortcut': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=CATEGORY_TYPE, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }