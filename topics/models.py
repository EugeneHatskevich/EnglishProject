from django.db import models
from django.utils.crypto import get_random_string


def create_random_id():
    random_id = get_random_string(
        length=12
    )
    return random_id


class Topics(models.Model):
    topic_id = models.CharField(
        max_length=255,
        default=create_random_id,
        unique=True,
        verbose_name='Внешний ID топика'
    )

    topic_name = models.CharField(
        max_length=255,
        verbose_name='Название топика',
        unique=True,
        default=''
    )

    topic_text = models.TextField(
        verbose_name='Текст топика',
        unique=True,
        default=''
    )

    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name = 'Топик'
        verbose_name_plural = 'Топики'

