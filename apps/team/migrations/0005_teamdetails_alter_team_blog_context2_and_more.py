# Generated by Django 4.2.6 on 2023-11-03 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_team_blog_context2_team_blog_title2_team_image_blog2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=155, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='team/details', verbose_name='фото')),
                ('end', models.CharField(max_length=155, verbose_name='Конец')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'ДЕтально Просмотр Команды',
            },
        ),
        migrations.AlterField(
            model_name='team',
            name='blog_context2',
            field=models.CharField(max_length=255, verbose_name='Описание Блога - 2'),
        ),
        migrations.AlterField(
            model_name='team',
            name='blog_title2',
            field=models.CharField(max_length=155, verbose_name='Заголовка Блога - 2'),
        ),
        migrations.AlterField(
            model_name='team',
            name='image_blog2',
            field=models.ImageField(upload_to='team-details', verbose_name='Фото Блога - 2'),
        ),
    ]