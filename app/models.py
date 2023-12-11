from django.db import models

# Create your models here.
class Task(models.Model):
    zadacha = models.CharField('Задача', max_length=500)
    nomer = models.PositiveIntegerField('Вопрос №', default=0)
    def __str__(self):
        return self.zadacha
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Kol(models.Model):
    koli = models.PositiveIntegerField('Количество заданий', default=1)
    foli = models.TextField(default='1')
    def __str__(self):
        return self.foli
    class Meta:
        verbose_name = 'Количество'
        verbose_name_plural = 'Количество'