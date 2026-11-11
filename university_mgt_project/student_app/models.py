from datetime import date

from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
)
from django.db import models
from django.utils import timezone

from .enumerations import (
    AcademicLevel,
    CourseType,
    Gender,
    GradeName,
    InscriptionStatus,
    Semester,
    TeacherRank,
)


class Student(models.Model):
    inscriptionNumber = models.PositiveBigIntegerField(primary_key=True)
    cin = models.CharField(
        max_length=8,
        unique=True,
        validators=[MaxLengthValidator(8), MinLengthValidator(8)],
    )
    name = models.CharField(max_length=50)
    familyName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default="")
    address = models.CharField(max_length=255, blank=True, default="")
    gender = models.CharField(
        max_length=1, choices=Gender.choices, default=Gender.UNSPECIFIED
    )
    level = models.CharField(
        max_length=2, choices=AcademicLevel.choices, default=AcademicLevel.L1
    )
    bio = models.TextField(blank=True, default="")
    birthday = models.DateField(default=date(2005, 1, 1))
    photo = models.ImageField(upload_to="images/student", blank=True, null=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "student"
        verbose_name = "student"
        verbose_name_plural = "students"
        ordering = ("familyName", "name")
        indexes = (
            models.Index(fields=["familyName", "name"]),
            models.Index(fields=["email"]),
        )

    def __str__(self):
        return f"{self.familyName} {self.name} ({self.inscriptionNumber})"


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    familyName = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default="")
    department = models.CharField(max_length=100, blank=True, default="")
    specialty = models.CharField(max_length=100, blank=True, default="")
    rank = models.CharField(
        max_length=20, choices=TeacherRank.choices, default=TeacherRank.LECTURER
    )
    bio = models.TextField(blank=True, default="")
    photo = models.ImageField(upload_to="images/teacher", blank=True, null=True)
    hiredAt = models.DateField(null=True, blank=True)
    isActive = models.BooleanField(default=True)
    createdAt = models.DateTimeField(default=timezone.now, editable=False)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "teacher"
        verbose_name = "teacher"
        verbose_name_plural = "teachers"
        ordering = ("familyName", "name")
        indexes = (
            models.Index(fields=["familyName", "name"]),
            models.Index(fields=["department"]),
        )

    def __str__(self):
        return f"{self.familyName} {self.name}"


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    startDate = models.DateTimeField(default=timezone.now, editable=False)
    endDate = models.DateTimeField()
    durationByWeek = models.DurationField()
    credits = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    semester = models.CharField(
        max_length=2, choices=Semester.choices, default=Semester.S1
    )
    maxStudents = models.PositiveSmallIntegerField(default=40)
    room = models.CharField(max_length=50, blank=True, default="")
    description = models.TextField(blank=True, default="")
    type = models.CharField(
        max_length=20, choices=CourseType.choices, default=CourseType.ONSITE
    )
    isActive = models.BooleanField(default=True)
    # relationship between Course and Teacher (*-1)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="courses",
    )
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "course"
        verbose_name = "course"
        verbose_name_plural = "courses"
        ordering = ("code", "title")
        indexes = (
            models.Index(fields=["code"]),
            models.Index(fields=["semester", "type"]),
        )

    def __str__(self):
        return f"{self.code} — {self.title}"


class Grade(models.Model):
    mark = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
    )
    maxMark = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=20,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
    )
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="grades"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="grades")
    # composite primary key
    pk = models.CompositePrimaryKey("student", "course", "gradeName")
    gradeName = models.CharField(max_length=30, choices=GradeName.choices)
    coefficient = models.FloatField(default=1.0, validators=[MinValueValidator(0.0)])
    justification = models.TextField(blank=True, default="")
    evaluatedAt = models.DateField(default=date.today, editable=False)

    class Meta:
        db_table = "grade"
        verbose_name = "grade"
        verbose_name_plural = "grades"
        ordering = ("-evaluatedAt",)
        unique_together = ("student", "course", "gradeName")

    def __str__(self):
        return f"{self.student} · {self.course} · {self.get_gradeName_display()}: {self.mark}/{self.maxMark}"


class Profile(models.Model):
    headline = models.CharField(max_length=120, blank=True, default="")
    skills = models.TextField(
        blank=True,
        default="",
        help_text="Comma-separated skills (e.g. Python, Django, SQL)",
    )
    portfolio = models.URLField(max_length=200, null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    # relationship between profile and student (1-1)
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="profile",
    )
    # relationship between profile and teacher (1-1)
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="profile",
    )
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "profile"
        verbose_name = "profile"
        verbose_name_plural = "profiles"
        constraints = (
            models.CheckConstraint(
                condition=(
                    models.Q(student__isnull=False) | models.Q(teacher__isnull=False)
                ),
                name="profile_owner_required",
            ),
        )

    def __str__(self):
        owner = self.student or self.teacher
        return f"Profile of {owner}" if owner else "Orphan profile"


class Inscription(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="inscriptions"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="inscriptions"
    )
    pk = models.CompositePrimaryKey("student", "course")
    date = models.DateField(default=date.today, editable=False)
    situation = models.CharField(
        max_length=25,
        choices=InscriptionStatus.choices,
        default=InscriptionStatus.PENDING,
    )
    remark = models.TextField(blank=True, default="")
    finalAverage = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(20)],
    )
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "inscription"
        verbose_name = "inscription"
        verbose_name_plural = "inscriptions"
        ordering = ("-date",)

    def __str__(self):
        return f"{self.student} → {self.course} [{self.get_situation_display()}]"
