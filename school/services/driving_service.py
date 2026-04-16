from ..models.student import Student
from ..models.driving_session import DrivingSession


class DrivingService:

    @staticmethod
    def calculate_total_hours(student: Student) -> float:
        sessions = DrivingSession.objects.filter(student=student)
        total_hours = sum(session.hours for session in sessions)
        return total_hours

    @staticmethod
    def update_student_hours(student: Student) -> None:
        total_hours = DrivingService.calculate_total_hours(student)
        student.total_driving_hours = total_hours
        student.save()
