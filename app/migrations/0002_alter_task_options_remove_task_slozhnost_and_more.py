# Generated by Django 4.2 on 2023-05-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.RemoveField(
            model_name='task',
            name='slozhnost',
        ),
        migrations.RemoveField(
            model_name='task',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='task',
            name='vopros',
        ),
        migrations.AddField(
            model_name='task',
            name='nomer',
            field=models.PositiveIntegerField(default=0, verbose_name='Вопрос №'),
        ),
        migrations.AlterField(
            model_name='task',
            name='zadacha',
            field=models.CharField(max_length=500, verbose_name='Задача'),
        ),
    ]
