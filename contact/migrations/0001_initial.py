# Generated by Django 4.2 on 2023-04-22 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contact.contact')),
            ],
        ),
        migrations.CreateModel(
            name='ContactMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contact.contact')),
            ],
        ),
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contact.contact')),
            ],
        ),
    ]
