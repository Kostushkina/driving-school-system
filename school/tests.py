from django.test import TestCase
from django.utils import timezone
from school.models.student import Student
from school.models.teacher import Teacher
from school.models.instructor import Instructor
from school.models.group import Group
from school.models.lesson import Lesson
from school.models.attendance import Attendance
from school.models.driving_session import DrivingSession
from school.models.test_result import TestResult
from school.services.attendance_service import AttendanceService
from school.services.driving_service import DrivingService
from school.services.admission_service import AdmissionService


class StudentModelTest(TestCase):
    def test_create_student(self):
        student = Student.objects.create(
            full_name="Иванов Иван",
            group="А-101",
            phone="+79991234567",
            email="ivanov@test.ru"
        )
        self.assertEqual(student.full_name, "Иванов Иван")
        self.assertEqual(student.group, "А-101")
        self.assertEqual(student.status, "active")

    def test_update_status(self):
        student = Student.objects.create(
            full_name="Петрова Анна",
            group="А-101",
            phone="+79991234568",
            email="petrova@test.ru"
        )
        student.status = "ready_for_exam"
        student.save()
        self.assertEqual(student.status, "ready_for_exam")


class AttendanceServiceTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            full_name="Сидоров Алексей",
            group="Б-202",
            phone="+79991234569",
            email="sidorov@test.ru"
        )
        self.teacher = Teacher.objects.create(
            full_name="Преподаватель Петров",
            email="teacher@test.ru",
            phone="+79991112233"
        )
        self.group = Group.objects.create(
            name="Группа А-101",
            teacher=self.teacher,
            start_date=timezone.now().date(),
            end_date=timezone.now().date()
        )
        self.lesson = Lesson.objects.create(
            group=self.group,
            teacher=self.teacher,
            topic="ПДД",
            date=timezone.now().date(),
            start_time="10:00:00",
            end_time="12:00:00"
        )

    def test_attendance_percentage_zero(self):
        percentage = AttendanceService.calculate_attendance_percentage(self.student)
        self.assertEqual(percentage, 0.0)

    def test_attendance_percentage_one_hundred(self):
        Attendance.objects.create(
            lesson=self.lesson,
            student=self.student,
            is_present=True
        )
        percentage = AttendanceService.calculate_attendance_percentage(self.student)
        self.assertEqual(percentage, 100.0)


class DrivingServiceTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            full_name="Водителев",
            group="В-303",
            phone="+79991234570",
            email="driver@test.ru"
        )
        self.instructor = Instructor.objects.create(
            full_name="Инструктор Иванов",
            email="instructor@test.ru",
            phone="+79991112234"
        )

    def test_total_hours_empty(self):
        hours = DrivingService.calculate_total_hours(self.student)
        self.assertEqual(hours, 0.0)

    def test_total_hours_with_sessions(self):
        DrivingSession.objects.create(
            student=self.student,
            instructor=self.instructor,
            date=timezone.now().date(),
            hours=2.5
        )
        hours = DrivingService.calculate_total_hours(self.student)
        self.assertEqual(hours, 2.5)


class AdmissionServiceTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            full_name="Экзаменов",
            group="Г-404",
            phone="+79991234571",
            email="exam@test.ru"
        )

    def test_not_ready(self):
        self.student.attendance_percentage = 50.0
        self.student.theory_test_passed = False
        self.student.total_driving_hours = 25.0
        is_ready = AdmissionService.check_admission_requirements(self.student)
        self.assertFalse(is_ready)

    def test_ready(self):
        self.student.attendance_percentage = 95.0
        self.student.theory_test_passed = True
        self.student.total_driving_hours = 55.0
        is_ready = AdmissionService.check_admission_requirements(self.student)
        self.assertTrue(is_ready)

    def test_boundary_values(self):
        self.student.attendance_percentage = 90.0
        self.student.theory_test_passed = True
        self.student.total_driving_hours = 50.0
        is_ready = AdmissionService.check_admission_requirements(self.student)
        self.assertTrue(is_ready)


class TestResultTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            full_name="Тестов",
            group="Д-505",
            phone="+79991234573",
            email="test@test.ru"
        )

    def test_passed(self):
        result = TestResult.objects.create(
            student=self.student,
            score=18,
            total_questions=20,
            passed=True
        )
        self.assertTrue(result.passed)

    def test_failed(self):
        result = TestResult.objects.create(
            student=self.student,
            score=10,
            total_questions=20,
            passed=False
        )
        self.assertFalse(result.failed)