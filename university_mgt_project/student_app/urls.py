"""
student_app URL routes (included under /api/ by the project urls).

DefaultRouter generates CRUD routes + every @action defined in views.py.

Custom action catalog (path comments match views.py)
----------------------------------------------------
Students
  EASY     GET  /api/students/count/
  EASY     GET  /api/students/{inscriptionNumber}/full-name/
  MEDIUM   GET  /api/students/by-level/?level=L1
  MEDIUM   POST /api/students/{inscriptionNumber}/deactivate/
  ADVANCED GET  /api/students/{inscriptionNumber}/transcript/

Teachers
  EASY     GET  /api/teachers/active/
  MEDIUM   GET  /api/teachers/{id}/courses/
  ADVANCED GET  /api/teachers/{id}/workload/

Courses
  EASY     GET  /api/courses/by-type/?type=online
  MEDIUM   GET  /api/courses/{id}/enrolled-students/
  ADVANCED POST /api/courses/{id}/enroll/
  ADVANCED GET  /api/courses/{id}/stats/

Grades
  EASY     GET  /api/grades/high-scores/
  MEDIUM   GET  /api/grades/by-course/?course_id=1
  ADVANCED GET  /api/grades/course-average/?course_id=1

Profiles
  EASY     GET  /api/profiles/with-github/
  MEDIUM   GET  /api/profiles/search/?q=django

Inscriptions
  EASY     GET  /api/inscriptions/pending/
  MEDIUM   POST /api/inscriptions/set-status/
  ADVANCED POST /api/inscriptions/bulk-accept/
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CourseViewSet,
    GradeViewSet,
    InscriptionViewSet,
    ProfileViewSet,
    StudentViewSet,
    TeacherViewSet,
)

# trailing_slash=True is the Django/DRF default (URLs end with /)
router = DefaultRouter()
router.register(r"students", StudentViewSet, basename="student")
router.register(r"teachers", TeacherViewSet, basename="teacher")
router.register(r"courses", CourseViewSet, basename="course")
router.register(r"grades", GradeViewSet, basename="grade")
router.register(r"profiles", ProfileViewSet, basename="profile")
router.register(r"inscriptions", InscriptionViewSet, basename="inscription")

urlpatterns = [
    # CRUD + all @action custom routes from the ViewSets above
    path("", include(router.urls)),
]
