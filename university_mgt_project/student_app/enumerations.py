from django.db import models
class CourseType(models.TextChoices):
    ONLINE='Online Course'
    ONSITE='Presential Course'
    HYBRID='Hybrid Course'

class InscriptionStatus(models.TextChoices):
    ACCEPTED='accepted inscription'
    ABORTED='aborted inscription'
    PENDING='pending inscription'
    REJECTED='rejected inscription'
    CANCELLED='cancelled inscription'
    COMPLETED='completed inscription'


class GradeName(models.TextChoices):
    EXAM='exam'
    PROJECT='project'
    HOMEWORK='homework'
    QUIZ='quiz'
    CAN='Continuous assessment'
    OTHER='other'
