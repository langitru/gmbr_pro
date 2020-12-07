from django.db import models

# Create your models here.
class Posts(models.Model):

    title = models.CharField('Название', max_length=180, default='')
    anons = models.CharField('Анонс', max_length=255, default='')
    full_text = models.TextField('Статья')
    date_public = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'