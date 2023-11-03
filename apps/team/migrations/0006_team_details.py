# Generated by Django 4.2.6 on 2023-11-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_teamdetails_alter_team_blog_context2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Заголовка')),
                ('context', models.CharField(max_length=155, verbose_name='Описание')),
                ('text', models.TextField(max_length=155, verbose_name='Текс')),
                ('image', models.ImageField(upload_to='team/details1', verbose_name='Фото')),
                ('text1', models.CharField(max_length=100, verbose_name='Колонка 1')),
                ('text2', models.CharField(max_length=100, verbose_name='Колонка 2')),
                ('text3', models.CharField(max_length=100, verbose_name='Колонка 3')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройка Команды',
            },
        ),
    ]
