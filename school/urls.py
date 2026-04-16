# school/urls.py
from django.urls import path
from . import api

urlpatterns = [
    path('students/rating/', api.student_rating, name='student-rating'),
]