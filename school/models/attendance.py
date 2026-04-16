from django.db import models
from .lesson import Lesson
from .student import Student


class Attendance(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name="Занятие"
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendances',
        verbose_name="Студент"
    )
    is_present = models.BooleanField(default=False, verbose_name="Присутствовал")
    marked_at = models.DateTimeField(auto_now_add=True, verbose_name="Время отметки")

    class Meta:
        unique_together = ('lesson', 'student')

    def __str__(self):
        status = "Присутствовал" if self.is_present else "Отсутствовал"
        return f"{self.student.full_name} - {self.lesson.topic} - {status}"
