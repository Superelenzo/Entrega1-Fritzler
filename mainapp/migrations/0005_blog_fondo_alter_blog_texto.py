# Generated by Django 4.2.5 on 2023-10-19 16:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_rename_ejemplo_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='fondo',
            field=models.ImageField(blank=True, null=True, upload_to='fondos'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='texto',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
