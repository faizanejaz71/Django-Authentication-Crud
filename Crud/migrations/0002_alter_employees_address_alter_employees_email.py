# Generated by Django 5.1.2 on 2024-10-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]