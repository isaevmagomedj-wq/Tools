from django.conf import settings
from django.db import models

class Category(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    name = models.CharField(max_length=50, verbose_name='Имя')

    def __str__(self):
        return f'{self.name}'

class Tools(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    name = models.CharField(max_length=50, verbose_name='Имя')
    specifications = models.TextField(blank=True, null=True, verbose_name='Описание')
    weight = models.CharField(max_length=32, verbose_name='Вес')
    model = models.CharField(max_length=32, verbose_name='Модель')
    warranty = models.CharField(max_length=10, verbose_name='Гарантия')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(verbose_name='Изображение')
    publication_date = models.DateField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.name}'

class FeedBack(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    body = models.TextField(verbose_name='Комментарий')
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE, verbose_name='Инструмент')

    def __str__(self):
        return f"{self.author}"
