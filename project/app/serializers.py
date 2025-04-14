from rest_framework import serializers
from .models import Attendance, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status', 'student_name']