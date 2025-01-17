# Вторая модель
from django.db import models


class SecondReceiver(models.Model):
    cost = models.IntegerField()
    bool = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'SecondReceiver'
        verbose_name = 'SecondReceiver'