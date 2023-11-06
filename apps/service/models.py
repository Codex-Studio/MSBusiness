from django.db import models

class Service(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    context = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='service',
        verbose_name='Фото'
    )
    number_blog = models.CharField(
        max_length=50,
        verbose_name='Номер Блога'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши Услуги'
        

################################SERVICE-DETAILS
class Details(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    text = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='service_details',
        verbose_name='Фото КОманды'
    )
    geografi_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Географий'
    )
    geografy_image = models.ImageField(
        upload_to='geografi',
        verbose_name='Фото Географий'
    )
    escort_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Сопровождение'
    )
    escort_context = models.TextField(
        verbose_name='Текст'
    )
    escort_image = models.ImageField(
        upload_to='escort',
        verbose_name='Сопровождение Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name =''
        verbose_name_plural = 'Настройка всего Примущество'

ICON = (
    ("Стратегическое Консультирование", "Стратегическое Консультирование"),
    ("Финансовое Планирование", "Финансовое Планирование"),
    ("Достижение Результатов", "Достижение Результатов"),
    ("Поддержка На Всех Этапах", "Поддержка На Всех Этапах"),
)

class ServiceDetails(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Колонка для Географий',
        blank=True, null=True
    )
    service_title = models.CharField(
        max_length=155,
        verbose_name='Колонки для Консалтинговых Услуг',
        blank=True, null=True
    )        
    icon = models.CharField(
        choices=ICON,
        max_length=50,
        verbose_name='Выберите иконку',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'География и Услуга'



class DetailsAll(models.Model):
    team_title = models.CharField(
        max_length=155,
        verbose_name='Колонки Команды'
    )
    team_title2 = models.CharField(
        max_length=155,
        verbose_name='Колонки Команды - 2'
    )
    escort_title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Сопровождение'
    )
    escort_text = models.CharField(
        max_length=255,
        verbose_name='Описание Сопровождение'
    )

    def __str__(self):
        return self.team_title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Бизнесс и Команда'

