from django.db import models
from .student import Student
from .instructor import Instructor


class DrivingSession(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='driving_sessions',
        verbose_name="Студент"
    )
    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.CASCADE,
        related_name='driving_sessions',
        verbose_name="Инструктор"
    )
    date = models.DateField(verbose_name="Дата")
    hours = models.FloatField(verbose_name="Количество часов")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return f"{self.student.full_name} - {self.instructor.full_name} - {self.hours}ч"

    class Meta:
        verbose_name = "Занятие по вождению"
        verbose_name_plural = "Занятия по вождению"
