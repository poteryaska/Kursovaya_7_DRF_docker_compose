from rest_framework.serializers import ValidationError
from django.utils import timezone


# В связанные привычки могут попадать только привычки с признаком приятной привычки
class RelatedHabitValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        for field in self.fields:
            related_habit = value.get(field)
            if related_habit:
                if related_habit and not related_habit.is_pleasurable:
                    raise ValidationError('Связанная привычка должна быть приятной')


# У приятной привычки не может быть вознаграждения или связанной привычки
class PleasantHabitValidator:
    def __call__(self, value):
        is_pleasant = value.get('is_pleasant')
        reward = value.get('reward')
        related_habit = value.get('related_habit')

        if is_pleasant:
            if reward:
                raise ValidationError('У приятной привычки не может быть вознаграждения.')
            if related_habit:
                raise ValidationError('У приятной привычки не может быть связанной привычки.')
        return value


# Нельзя выполнять привычку реже, чем 1 раз в 7 дней
class FrequencyHabitValidator:
    def __call__(self, value):
        frequency = value.get('frequency')

        if frequency == 'Еженедельная':
            time_to_perform = value.get('time_to_perform')
            if time_to_perform:
                difference = (timezone.now() - time_to_perform).days
                if difference < 7:
                    raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
        return value