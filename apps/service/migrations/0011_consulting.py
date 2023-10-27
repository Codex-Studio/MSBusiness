# Generated by Django 4.2.6 on 2023-10-27 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_teamwide'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('context', models.CharField(max_length=255, verbose_name='Описание')),
                ('icon', models.CharField(choices=[('Стратегическое Консультирование', 'Стратегическое Консультирование'), ('Финансовое Планирование', 'Финансовое Планирование'), ('Достижение Результатов', 'Достижение Результатов'), ('Поддержка На Всех Этапах', 'Поддержка На Всех Этапах')], max_length=155, verbose_name='Выберите Иконку')),
                ('icon_context', models.CharField(max_length=255, verbose_name='Заголовка иконки')),
                ('icon_end', models.CharField(max_length=100, verbose_name='Конец Консалтингов')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Настройка Консалтингов',
            },
        ),
    ]
