from django.db import models
from django_resized.forms import ResizedImageField


# Create your models here.
class Team(models.Model):
    id_team = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    job = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to='teacher_img/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    descriptions = models.TextField(
        max_length=255,
        verbose_name="Описание человека"
    )
    phone_doctor = models.CharField(
        max_length=255,
        verbose_name='номер',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"

class Contact_Team(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя"
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона"
    )
    message = models.TextField(
        verbose_name="Введите ваше сообщение"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оставленный отзыв доктору"
        verbose_name_plural = "Оставленный отзыв доктору"