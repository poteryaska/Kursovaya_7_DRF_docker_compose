from rest_framework import serializers
from habits.models import Habit
from habits.validators import RelatedHabitValidator, PleasantHabitValidator, FrequencyHabitValidator


def validate_time_to_perform(value):
    if value.total_seconds() > 120:
        raise serializers.ValidationError('Время выполнения не должно превышать 2 минуты.')


class HabitSerializer(serializers.ModelSerializer):
    time_to_perform = serializers.CharField(validators=[validate_time_to_perform])

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedHabitValidator(fields=['related_habit']),
            PleasantHabitValidator(),
            FrequencyHabitValidator()
        ]

    # validator проверки полей: связанной привычки и вознаграждения
    def validate(self, data):
        related_habit = data.get('related_habit')
        reward = data.get('reward')

        if related_habit and reward:
            raise serializers.ValidationError('Нельзя одновременно указать связанную привычку и вознаграждение')

        return data