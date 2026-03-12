from django.conf import settings
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tools(models.Model):
    name = models.CharField(max_length=50)
    specifications = models.TextField(blank=True, null=True)
    weight = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    warranty = models.CharField(max_length=10)
    rating = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class FeedBack(models.Model):
    author = models.CharField(max_length=32)
    body = models.TextField()
    tool = models.ForeignKey(Tools, on_delete=models.CASCADE)

    def __str__(self):
        return self.author
