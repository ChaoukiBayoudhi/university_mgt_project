from rest_framework import viewsets
from .models import Student, Teacher, Course, Grade, Profile, Inscription
from .serializers import StudentSerializer, TeacherSerializer, CourseSerializer, GradeSerializer, ProfileSerializer, InscriptionSerializer
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer
    #permissio_class=[IsAuthenticated]
    #authentication_classes=[TokenAuthentication]

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset=Grade.objects.all()
    serializer_class=GradeSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

class InscriptionViewSet(viewsets.ModelViewSet):
    queryset=Inscription.objects.all()
    serializer_class=InscriptionSerializer
    