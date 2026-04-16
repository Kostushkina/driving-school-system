from ..models.student import Student


class AdmissionService:

    MIN_ATTENDANCE_PERCENTAGE = 90.0
    MIN_DRIVING_HOURS = 50.0

    @staticmethod
    def check_admission_requirements(student: Student) -> bool:
        """Проверяет условия допуска к экзамену"""
        conditions_met = (
            student.attendance_percentage >= AdmissionService.MIN_ATTENDANCE_PERCENTAGE
            and student.theory_test_passed
            and student.total_driving_hours >= AdmissionService.MIN_DRIVING_HOURS
        )
        return conditions_met

    @staticmethod
    def update_student_status(student: Student) -> bool:
        """Обновляет статус студента"""
        current_status = student.status
        is_ready = AdmissionService.check_admission_requirements(student)

        if is_ready and current_status != 'ready_for_exam':
            student.status = 'ready_for_exam'
            student.save()
            return True
        elif not is_ready and current_status == 'ready_for_exam':
            student.status = 'active'
            student.save()
            return True
        return False

    @staticmethod
    def get_admission_report() -> list:
        """Возвращает список студентов, готовых к экзамену"""
        ready_students = Student.objects.filter(status='ready_for_exam')
        return [
            {
                'full_name': s.full_name,
                'group': s.group,
                'attendance': s.attendance_percentage,
                'driving_hours': s.total_driving_hours
            }
            for s in ready_students
        ]