from django.core.validators import (MaxLengthValidator,
                                        MinLengthValidator)
from django.db import models
from django.utils import timezone
from .enumerations import CourseType, GradeName,InscriptionStatus

class Student(models.Model):
    inscriptionNumber=models.PositiveBigIntegerField(primary_key=True)
    cin=models.CharField(max_length=8,
                    validators=[MaxLengthValidator(8),MinLengthValidator(8)])
    name=models.CharField(max_length=50)
    familyName=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    bio=models.TextField(null=True, blank=True)
    birthday=models.DateField(default=timezone.datetime(2005,1,1))
    photo=models.ImageField(upload_to='images/student')
    class Meta:
        db_table = 'student'
        #ordering = ['name'] #ascending order
        #or
        ordering = ['-name'] #descending order


class Teacher(models.Model):
    name=models.CharField(max_length=50)
    familyName=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    bio=models.TextField(null=True, blank=True)
    photo=models.ImageField(upload_to='images/teacher')
    class Meta:
        db_table = 'teacher'




class Course(models.Model):
    title=models.CharField(max_length=100)
    startDate=models.DateTimeField(auto_now_add=True)
    endDate=models.DateTimeField()
    durationByWeek=models.DurationField()
    credits=models.PositiveSmallIntegerField()
    description=models.TextField()
    type=models.CharField(max_length=20, choices=CourseType.choices,
                                default=CourseType.ONSITE)
    #relationship between Course and Teacher (*-1)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    class Meta:
        db_table = 'course'

class Grade(models.Model):
    mark=models.DecimalField(max_digits=4,decimal_places=2)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    pk=models.CompositePrimaryKey('student', 'course', 'gradeName')
    gradeName=models.CharField(max_length=30, choices=GradeName.choices)
    coefficient=models.FloatField()
    justification=models.TextField(null=True)

    class Meta:
        db_table = 'grade'
        unique_together = ('student', 'course', 'gradeName')

class Profile(models.Model):
    portfolio=models.URLField(max_length=200, null=True, blank=True)
    linkedin=models.URLField(max_length=200, null=True, blank=True)
    github=models.URLField(max_length=200, null=True, blank=True)
    website=models.URLField(max_length=200, null=False, blank=False)
    #relationship between profile and student (1-1)
    student=models.OneToOneField(Student, on_delete=models.CASCADE,
                                null=True, blank=True)
    #relationship between profile and teacher (1-1)
    teacher=models.OneToOneField(Teacher, on_delete=models.CASCADE,
                        null=True, blank=True)
    class Meta:
        db_table = 'profile'

class Inscription(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    pk=models.CompositePrimaryKey('student','course')
    date=models.DateField(auto_now=True)
    situation=models.CharField(max_length=25,choices=InscriptionStatus.choices)
    class Meta:
        db_table = 'inscription'
