# Generated by Django 4.2.5 on 2023-10-03 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_delete_curso_ejemplo_autor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ejemplo',
            new_name='Blog',
        ),
    ]