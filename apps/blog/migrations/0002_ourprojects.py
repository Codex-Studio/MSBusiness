# Generated by Django 4.2.7 on 2023-11-05 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('descriptio', models.CharField(max_length=255, verbose_name='Номер колонки')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наши проекты',
            },
        ),
    ]