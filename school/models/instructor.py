from django.db import models


class Instructor(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    car_number = models.CharField(
        max_length=10,
        blank=True,
        verbose_name="Номер автомобиля"
    )

    def __str__(self):
        return f"{self.full_name} ({self.car_number})"

    class Meta:
        verbose_name = "Инструктор"
        verbose_name_plural = "Инструкторы"
