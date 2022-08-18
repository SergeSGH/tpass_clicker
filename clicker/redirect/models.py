from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Link(models.Model):
    short_link = models.TextField(
        verbose_name='Короткая ссылка',
        help_text='Короткая ссылка',
        db_index=True
    )

    original_link = models.TextField(
        verbose_name='Первоначальная ссылка',
        help_text='Первоначальная ссылка'
    )

    expires = models.DateTimeField(
        verbose_name='Дата прекращения действия',
        help_text='Дата прекращения действия'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return str(self.original_link[:15])
