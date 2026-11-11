from rest_framework import serializers

from .models import Course, Grade, Inscription, Profile, Student, Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "inscriptionNumber",
            "cin",
            "name",
            "familyName",
            "email",
            "phone",
            "address",
            "gender",
            "level",
            "bio",
            "birthday",
            "photo",
            "isActive",
            "createdAt",
            "updatedAt",
        )
        read_only_fields = ("createdAt", "updatedAt")


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "id",
            "name",
            "familyName",
            "email",
            "phone",
            "department",
            "specialty",
            "rank",
            "bio",
            "photo",
            "hiredAt",
            "isActive",
            "createdAt",
            "updatedAt",
        )
        read_only_fields = ("id", "createdAt", "updatedAt")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "code",
            "title",
            "startDate",
            "endDate",
            "durationByWeek",
            "credits",
            "semester",
            "maxStudents",
            "room",
            "description",
            "type",
            "isActive",
            "teacher",
            "updatedAt",
        )
        read_only_fields = ("id", "startDate", "updatedAt")


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = (
            "mark",
            "maxMark",
            "student",
            "course",
            "gradeName",
            "coefficient",
            "justification",
            "evaluatedAt",
        )
        read_only_fields = ("evaluatedAt",)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "headline",
            "skills",
            "portfolio",
            "linkedin",
            "github",
            "website",
            "student",
            "teacher",
            "updatedAt",
        )
        read_only_fields = ("id", "updatedAt")


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = (
            "student",
            "course",
            "date",
            "situation",
            "remark",
            "finalAverage",
            "updatedAt",
        )
        read_only_fields = ("date", "updatedAt")
