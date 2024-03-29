from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название товара')
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    # author = models.ForeignKey('users.User', on_delete=models.CASCADE, default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']

    def str(self):
        return self.text
