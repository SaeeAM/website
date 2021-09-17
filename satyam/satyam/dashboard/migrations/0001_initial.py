# Generated by Django 3.1 on 2020-11-11 13:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True, max_length=200)),
                ('document', models.FileField(upload_to='service/document/')),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('default', 'Choose Option'), ('digital', 'Digital Service'), ('govtscheme', 'Govt Service'), ('student', 'Student Service'), ('common', 'Common Service'), ('business', 'Business Service')], default='default', max_length=80)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('discription', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'service',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('trackid', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.URLField(default='')),
                ('comp_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.costumer')),
            ],
            options={
                'verbose_name': 'track',
                'verbose_name_plural': 'Track',
                'ordering': ['comp_time'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', ckeditor.fields.RichTextField()),
                ('service_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.service')),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'document',
                'ordering': ['document'],
            },
        ),
        migrations.AddField(
            model_name='costumer',
            name='choose_service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.service'),
        ),
        migrations.AddField(
            model_name='costumer',
            name='service_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.document'),
        ),
    ]