from django.db import models
from django.utils import timezone

# Create your models here.
class Posts(models.Model):

    title = models.CharField('Название', max_length=180, default='')
    anons = models.CharField('Анонс', max_length=255, default='')
    full_text = models.TextField('Статья')
    date_public = models.DateTimeField('Дата публикации', help_text='Укажите дату публикации!' )

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/posts/{self.id}'


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'