from django.db import models

class Post(models.Model):
    title = models.CharField('заголовок', max_length = 50)
    content = models.TextField('текст')
    created_at = models.DateTimeField('дата публикации')
    image = models.CharField('изображение', max_length = 200)