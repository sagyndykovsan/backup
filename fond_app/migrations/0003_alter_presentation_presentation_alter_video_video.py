# Generated by Django 4.2 on 2023-04-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fond_app', '0002_alter_book_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='presentation',
            field=models.FileField(upload_to='pptx'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='video'),
        ),
    ]
