from rest_framework import serializers
from .models import Student, Teacher, Course, Grade, Profile, Inscription
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        #fields='__all__'
        fields=('inscriptionNumber', 'name', 'familyName', 'email','birthday')
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields='__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grade
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Inscription
        fields='__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'
