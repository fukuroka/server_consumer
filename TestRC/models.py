from django.db import models


class Receiver(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Receivers'
        verbose_name = 'Receiver'