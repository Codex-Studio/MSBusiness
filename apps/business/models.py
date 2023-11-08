from django.db import models

# Create your models here.

ICON = (
    ("Локальная Экспертиза, Мировой Опыт", "Локальная Экспертиза, Мировой Опыт"),
    ("Преимущество Многокультурного Окружения", "Преимущество Многокультурного Окружения"),
    ("Сотрудничество Через Расстояние", "Сотрудничество Через Расстояние"),
    ("Мировые Достижения", "Мировые Достижения"),
    ("Местное присутствие ", "Местное присутствие "),
    ("Многогранное понимание культур ", "Многогранное понимание культур "),
)

class Benefist(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        upload_to='benefist',
        verbose_name='Фото'
    )
    icon = models.CharField(
        choices=ICON,
        max_length=155,
        verbose_name='Иконка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Широкая География'
        verbose_name_plural = 'Широкая География'


ICON_RANGE = (
    ("Стратегическое Консультирование", "Стратегическое Консультирование"),
    ("Финансовый Консалтинг", "Финансовый Консалтинг"),
    ("Маркетинговые Консультации", "Маркетинговые Консультации"),
    ("Поддержка На Всех Этапах", "Поддержка На Всех Этапах"),
    ("Достижение Результатов", "Достижение Результатов"),
    ("Финансовое Планирование", "Финансовое Планирование"),

)

class Range(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    image = models.ImageField(
        upload_to='range/',
        verbose_name='Фото'
    )
    icon = models.CharField(
        choices=ICON_RANGE,
        max_length=155,
        verbose_name='Иконка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Широкий Спектр'
