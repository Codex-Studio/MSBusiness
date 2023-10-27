# Generated by Django 4.2.6 on 2023-10-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_services_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовка')),
                ('context', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.RemoveField(
            model_name='services',
            name='context',
        ),
        migrations.RemoveField(
            model_name='services',
            name='title',
        ),
    ]
