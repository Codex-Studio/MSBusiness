from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name='Фото'
    )
    email = models.CharField(
        max_length=155,
        verbose_name='Адрес почты',
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name='Номер Телефона',
        blank=True, null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    schedule = models.CharField(
        max_length=155,
        verbose_name='Расписание',
        blank=True, null=True
    )
    facebook = models.CharField(
        max_length=155,
        verbose_name='Файсбук',
        blank=True, null=True
    )
    skype = models.CharField(
        max_length=155,
        verbose_name='Скайп',
        blank=True, null=True
    )
    instagram = models.CharField(
        max_length=155,
        verbose_name='Инстаграмм',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='index',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настройки главной страницы'

ICON = (
    ("ИЗУЧЕНИЕ", "ИЗУЧЕНИЕ"),
    ("РАЗРАБОТКА", "РАЗРАБОТКА"),
    ("ЗАПУСК", "ЗАПУСК")
)


class OperationProcess(models.Model):
    image = models.ImageField(
        upload_to='process',
        verbose_name='фото'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    descriptions = models.CharField(
        max_length=300,
        verbose_name='Описание'
    )
    number = models.CharField(
        max_length=100,
        verbose_name='Номер Блога'
    )
    icon = models.CharField(
        max_length=50,
        choices=ICON,
        verbose_name = 'Выберите Иконку'
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Процесс работы'



class Benefits(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = models.CharField(
        max_length=355,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Преимущества'


class Contact(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка Контакта'
    )
    name_surname = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        blank=True, null=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name='Номер Телефона',
        blank=True, null=True
    )
    email = models.CharField(
        max_length=155,
        verbose_name='Адресс почты',
        blank=True, null=True
    )
    limit = models.CharField(
        max_length=155,
        verbose_name='Лимит',
        blank=True,null=True
    )
    message = models.CharField(
        max_length=355,
        verbose_name='Сообщение',
        blank=True, null=True
    )
    cause = models.CharField(
        max_length=355,
        verbose_name='Причина',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Контакты и заявка'

class Partner(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка',
        blank=True, null=True
    )
    description = models.CharField(
        max_length=255,
        verbose_name='описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='partner',
        verbose_name='Фото'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Партнеры'


class Project(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    ) 
    description = models.CharField(
        max_length=300,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Наши проекты'

class ProjectoFeatures(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name="about_us_images"
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Особенности проекта'
