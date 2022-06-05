from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Publication(models.Model):
    title = models.CharField(verbose_name='Заголовок публикации', max_length=100, blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Автор', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(verbose_name='Время создания', blank=True, null=True, default=now)
    text = models.TextField(verbose_name='Текст публикации')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
