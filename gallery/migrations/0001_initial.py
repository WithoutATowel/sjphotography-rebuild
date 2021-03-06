# Generated by Django 3.0.2 on 2020-01-14 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('cover_photo', models.FileField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('image', models.FileField(upload_to='')),
                ('uploaded_date', models.DateField(auto_now_add=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='gallery.Collection')),
            ],
        ),
    ]
