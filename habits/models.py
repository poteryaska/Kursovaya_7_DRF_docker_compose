from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    DAILY = 'Ежедневная'
    WEEKLY = 'Еженедельная'

    FREQUENCY_CHOICES = (
        (DAILY, 'Ежедневная'),
        (WEEKLY, 'Еженедельная'),

    )

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='владелец')
    place = models.CharField(max_length=50, verbose_name='место')
    timing = models.TimeField(verbose_name='время начала привычки')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                      verbose_name='связанная привычка', **NULLABLE)
    frequency = models.CharField(choices=FREQUENCY_CHOICES, default=DAILY, verbose_name='периодичность')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)
    time_to_perform = models.CharField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.timing} в {self.place} заниматься {self.action}'


    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'