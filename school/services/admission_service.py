from ..models.student import Student


class AdmissionService:

    MIN_ATTENDANCE_PERCENTAGE = 90.0
    MIN_DRIVING_HOURS = 50.0

    @staticmethod
    def check_admission_requirements(student: Student) -> bool:
        conditions_met = (
            student.attendance_percentage >= AdmissionService.MIN_ATTENDANCE_PERCENTAGE
            and student.theory_test_passed
            and student.total_driving_hours >= AdmissionService.MIN_DRIVING_HOURS
        )
        return conditions_met

    @staticmethod
    def update_student_status(student: Student) -> bool:
        current_status = student.status
        is_ready = AdmissionService.check_admission_requirements(student)

        if is_ready and current_status != 'ready_for_exam':
            student.status = 'ready_for_exam'
            student.save()
            return True
        return False
