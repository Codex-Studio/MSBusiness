# Generated by Django 4.2.6 on 2023-10-26 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='number',
            field=models.CharField(default=1, max_length=20, verbose_name='Номер Блога'),
            preserve_default=False,
        ),
    ]