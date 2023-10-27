# Generated by Django 4.2.6 on 2023-10-27 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_servicedetails_end_details_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовка')),
                ('title2', models.CharField(max_length=100, verbose_name='Заголовка - 2')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to='team/', verbose_name='Фотография команды')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наша команда',
            },
        ),
    ]
