# Generated by Django 3.1.1 on 2020-10-18 07:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201013_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]