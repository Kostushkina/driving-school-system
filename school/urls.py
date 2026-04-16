# school/urls.py
from django.urls import path
from . import api

urlpatterns = [
    path('students/rating/', api.student_rating, name='student-rating'),
]
urlpatterns = [
    path('students/rating/', api.student_rating, name='student-rating'),
    path('admission/report/', api.admission_report, name='admission-report'),
]
urlpatterns = [
    path('students/rating/', api.student_rating, name='student-rating'),
    path('admission/report/', api.admission_report, name='admission-report'),
    path('students/filter/', api.filter_students, name='filter-students'),
]