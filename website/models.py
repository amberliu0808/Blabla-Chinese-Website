from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# from ckeditor.fields import RichTextField
# from django_resized import ResizedImageField
from PIL import Image


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog')


types = Category.objects.all().values_list('name', 'name')
CATEGORY_TYPE = []
for item in types:
    CATEGORY_TYPE.append(item)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


# tags = Tag.objects.all().values_list('tag_name', 'tag_name')
# TAG_TYPE = []
# for tag in tags:
# TAG_TYPE.append(tag)


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_TYPE, default='Funny Stories')
    tag = models.CharField(max_length=255, choices=Tag.objects.all().values_list('tag_name', 'tag_name'),
                           default='humor')
    # content = models.TextField()
    # content = RichTextField(blank=True, null=True)
    content = models.TextField(default="content")
    shortcut = models.CharField(max_length=255)
    # thumbnail = ResizedImageField(size=[850, 530], blank=True, null=True, upload_to="images/")
    thumbnail = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="Amber Liu")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost', args=[self.slug])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.thumbnail.path)

        if img.height > 850 or img.width > 530:
            output_size = (850, 530)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)
