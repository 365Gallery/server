# Generated by Django 3.1.7 on 2021-05-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('file', models.ImageField(default='/', upload_to='media/')),
                ('src', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]
