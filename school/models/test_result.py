from django.db import models
from .student import Student


class TestResult(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='test_results',
        verbose_name="Студент"
    )
    score = models.IntegerField(verbose_name="Количество правильных ответов")
    total_questions = models.IntegerField(default=20, verbose_name="Всего вопросов")
    passed = models.BooleanField(default=False, verbose_name="Тест сдан")
    taken_at = models.DateTimeField(auto_now_add=True, verbose_name="Время прохождения")

    def __str__(self):
        return f"{self.student.full_name} - {self.score}/{self.total_questions}"

    class Meta:
        verbose_name = "Результат теста"
        verbose_name_plural = "Результаты тестов"
