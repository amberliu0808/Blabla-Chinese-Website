# Generated by Django 4.1 on 2022-08-31 03:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Funny Stories', 'Funny Stories'), ('Students Colorful Lives', 'Students Colorful Lives'), ('Daily', 'Daily'), ('Language Tips', 'Language Tips'), ('Resources', 'Resources')], default='Funny Stories', max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
