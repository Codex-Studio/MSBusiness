# Generated by Django 4.2.6 on 2023-10-28 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0048_application_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='klient/', verbose_name='Фото')),
                ('end_coment', models.CharField(max_length=100, verbose_name='Смотреть проекты')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наши клиенты',
            },
        ),
    ]
