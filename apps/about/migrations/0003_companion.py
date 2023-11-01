# Generated by Django 4.2.6 on 2023-10-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_end_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100, verbose_name='Заголовка Блога')),
                ('blog_context', models.CharField(max_length=100, verbose_name='Описание Блога')),
                ('title', models.CharField(max_length=100, verbose_name='ЗАголовка')),
                ('text1', models.TextField(verbose_name='Текс')),
                ('text2', models.TextField(verbose_name='Текст - 2')),
                ('image', models.ImageField(upload_to='companion/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наша компания',
            },
        ),
    ]