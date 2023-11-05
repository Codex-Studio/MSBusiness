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
        blank=True, null=True
    ) 
    context = models.TextField(
        verbose_name='Описание',
        blank=True, null=True
    )
    image = models.ImageField(
        upload_to='details',
        verbose_name='Фото',
        blank=True, null=True
    )
    kolonki = models.CharField(
        max_length=155,
        verbose_name='Колонки Блога',
        blank=True, null=True
    )
    review_blog = models.CharField(
        max_length=155,
        verbose_name='Блог Услуги',
        blank=True, null=True
    )
    business_blog = models.CharField(
        max_length=155,
        verbose_name='Заголовка',
        blank=True, null=True
    )
    business_context = models.CharField(
        max_length=300,
        verbose_name='Описание Бизнеса',
        blank=True, null=True
    )
    business_image = models.ImageField(
        upload_to='business',
        verbose_name='Фото'
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Настрокий детального Услуги'
