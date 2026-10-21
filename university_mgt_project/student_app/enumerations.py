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
