from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="Autor", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Título")
    text = models.TextField(verbose_name="Texto", max_length=1000)

    def __str__(self):
        return self.title
