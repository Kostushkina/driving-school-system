# school/api.py
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .services.admission_service import AdmissionService


class StudentRatingSerializer(serializers.ModelSerializer):
    is_ready_for_exam = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id', 'full_name', 'group', 'status',
            'attendance_percentage', 'total_driving_hours',
            'theory_test_passed', 'is_ready_for_exam'
        ]

    def get_is_ready_for_exam(self, obj):
        return AdmissionService.check_admission_requirements(obj)


@api_view(['GET'])
def student_rating(request):
    """API для получения рейтинга студентов"""
    students = Student.objects.all()
    serializer = StudentRatingSerializer(students, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def admission_report(request):
    """API для получения отчета о студентах, готовых к экзамену"""
    report = AdmissionService.get_admission_report()
    return Response(report)