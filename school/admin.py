from django.contrib import admin
from .models import (
    Student, Teacher, Instructor, Group, Lesson,
    Attendance, DrivingSession, TestResult
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'group', 'status',
        'attendance_percentage', 'total_driving_hours', 'theory_test_passed'
    )
    list_filter = ('status', 'group')
    search_fields = ('full_name', 'email')
    list_editable = ('theory_test_passed',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')
    search_fields = ('full_name', 'email')


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'car_number')
    search_fields = ('full_name', 'email')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'start_date', 'end_date')
    list_filter = ('teacher',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'group', 'teacher', 'date', 'start_time', 'end_time')
    list_filter = ('group', 'teacher', 'date')


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'is_present', 'marked_at')
    list_filter = ('is_present', 'lesson__group')
    list_editable = ('is_present',)


@admin.register(DrivingSession)
class DrivingSessionAdmin(admin.ModelAdmin):
    list_display = ('student', 'instructor', 'date', 'hours')
    list_filter = ('instructor', 'date')


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'score', 'total_questions', 'passed', 'taken_at')
    list_filter = ('passed', 'taken_at')
