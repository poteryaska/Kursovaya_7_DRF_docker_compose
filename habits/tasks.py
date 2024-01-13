from datetime import datetime
import pytz
from celery import shared_task
from habits.models import Habit
from habits.services import habit_scheduler


@shared_task
def every_day():
    timezone = pytz.timezone('Europe/Moscow')
    current_time_yek = datetime.now(timezone)
    current_time = current_time_yek.strftime('%H:%M')
    habits = Habit.objects.all()  # Получяем объекты Habit по фильтру раз в день

    for habit in habits:

        if habit.DAILY:
            if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                habit_scheduler(habit.get_habit)  # Выполняем отправку


        if habit.WEEKLY:
            if (current_time_yek - habit.create_time).days > 7:  # каждые 172 часа раз в 7 дня
                if current_time == habit.time_habit.strftime('%H:%M'):  # проверяем чч:мм отправки
                    habit_scheduler(habit.get_habit)