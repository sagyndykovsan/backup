# Generated by Django 4.2 on 2023-04-22 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contactaddress_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactaddress',
            options={'verbose_name': 'Contact address', 'verbose_name_plural': 'Contact address'},
        ),
    ]
