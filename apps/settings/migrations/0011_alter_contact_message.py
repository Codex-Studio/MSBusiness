# Generated by Django 4.2.7 on 2023-11-05 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_alter_partner_description_alter_partner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(blank=True, max_length=355, null=True, verbose_name='Сообщение'),
        ),
    ]