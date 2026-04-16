from ..models.student import Student
from ..models.attendance import Attendance


class AttendanceService:

    @staticmethod
    def calculate_attendance_percentage(student: Student) -> float:
        attendances = Attendance.objects.filter(student=student)
        total_lessons = attendances.count()

        if total_lessons == 0:
            return 0.0

        present_count = attendances.filter(is_present=True).count()
        percentage = (present_count / total_lessons) * 100
        return round(percentage, 2)

    @staticmethod
    def update_student_attendance(student: Student) -> None:
        percentage = AttendanceService.calculate_attendance_percentage(student)
        student.attendance_percentage = percentage
        student.save()
