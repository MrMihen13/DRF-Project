from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=126)
    body = models.CharField(verbose_name='Body', unique=True, max_length=256)
    done = models.BooleanField(verbose_name='Done')
    file = models.FileField(verbose_name='File', default=None, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
