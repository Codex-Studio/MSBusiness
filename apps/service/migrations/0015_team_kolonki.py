# Generated by Django 4.2.6 on 2023-11-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0014_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='kolonki',
            field=models.CharField(default=1, max_length=100, verbose_name='Колонки'),
            preserve_default=False,
        ),
    ]