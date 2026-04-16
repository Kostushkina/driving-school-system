from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('active', 'Обучается'),
        ('ready_for_exam', 'Допущен к экзамену'),
        ('graduated', 'Выпущен'),
    ]

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    group = models.CharField(max_length=20, verbose_name="Группа")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(unique=True, verbose_name="Email")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name="Статус"
    )
    attendance_percentage = models.FloatField(
        default=0.0,
        verbose_name="Процент посещаемости"
    )
    total_driving_hours = models.FloatField(
        default=0.0,
        verbose_name="Всего часов вождения"
    )
    theory_test_passed = models.BooleanField(
        default=False,
        verbose_name="Тест сдан"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
