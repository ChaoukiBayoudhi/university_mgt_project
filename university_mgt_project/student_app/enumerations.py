# pyright: reportAssignmentType=false
# TextChoices members are declared as str, but Django's API assigns (value, label) tuples.
from django.db import models


class CourseType(models.TextChoices):
    ONLINE = "online", "Online Course"
    ONSITE = "onsite", "On-site Course"
    HYBRID = "hybrid", "Hybrid Course"


class InscriptionStatus(models.TextChoices):
    ACCEPTED = "accepted", "Accepted inscription"
    ABORTED = "aborted", "Aborted inscription"
    PENDING = "pending", "Pending inscription"
    REJECTED = "rejected", "Rejected inscription"
    CANCELLED = "cancelled", "Cancelled inscription"
    COMPLETED = "completed", "Completed inscription"


class GradeName(models.TextChoices):
    EXAM = "exam", "Exam"
    PROJECT = "project", "Project"
    HOMEWORK = "homework", "Homework"
    QUIZ = "quiz", "Quiz"
    CAN = "can", "Continuous assessment"
    OTHER = "other", "Other"


class Gender(models.TextChoices):
    FEMALE = "F", "Female"
    MALE = "M", "Male"
    OTHER = "O", "Other"
    UNSPECIFIED = "U", "Prefer not to say"


class AcademicLevel(models.TextChoices):
    L1 = "L1", "Licence 1"
    L2 = "L2", "Licence 2"
    L3 = "L3", "Licence 3"
    M1 = "M1", "Master 1"
    M2 = "M2", "Master 2"


class Semester(models.TextChoices):
    S1 = "S1", "Semester 1"
    S2 = "S2", "Semester 2"
    SUMMER = "SU", "Summer"


class TeacherRank(models.TextChoices):
    ASSISTANT = "assistant", "Assistant"
    LECTURER = "lecturer", "Lecturer"
    ASSOCIATE = "associate", "Associate Professor"
    PROFESSOR = "professor", "Professor"
    CONTRACT = "contract", "Contract Teacher"
