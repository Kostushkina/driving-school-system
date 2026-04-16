from django.db import models


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
