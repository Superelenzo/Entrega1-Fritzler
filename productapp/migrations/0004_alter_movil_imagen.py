# Generated by Django 4.2.5 on 2023-10-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_alter_movil_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/galeria'),
        ),
    ]
