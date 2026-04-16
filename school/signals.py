from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Attendance, DrivingSession, TestResult
from .services import AttendanceService, DrivingService, AdmissionService


@receiver([post_save, post_delete], sender=Attendance)
def update_student_on_attendance_change(sender, instance, **kwargs):
    AttendanceService.update_student_attendance(instance.student)
    AdmissionService.update_student_status(instance.student)


@receiver([post_save, post_delete], sender=DrivingSession)
def update_student_on_driving_change(sender, instance, **kwargs):
    DrivingService.update_student_hours(instance.student)
    AdmissionService.update_student_status(instance.student)


@receiver(post_save, sender=TestResult)
def update_student_on_test_change(sender, instance, **kwargs):
    student = instance.student
    student.theory_test_passed = instance.passed
    student.save()
    AdmissionService.update_student_status(student)
