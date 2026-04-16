from django.db import models
from .group import Group
from .teacher import Teacher


class Lesson(models.Model):
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name="Группа"
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name="Преподаватель"
    )
    topic = models.CharField(max_length=255, verbose_name="Тема занятия")
    date = models.DateField(verbose_name="Дата")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")

    def __str__(self):
        return f"{self.topic} - {self.date}"

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"
