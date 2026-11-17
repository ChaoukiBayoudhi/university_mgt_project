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
  ADVANCED GET  /api/students/by-level-stats/?min=2          (GROUP BY + HAVING)
  ADVANCED GET  /api/students/with-avg-mark/?min_avg=10      (Subquery + annotate)
  ADVANCED GET  /api/students/demo-aggregate/               (aggregate = 1 summary)
  ADVANCED GET  /api/students/demo-annotate/                (annotate = per-row column)

Teachers
  EASY     GET  /api/teachers/active/
  MEDIUM   GET  /api/teachers/{id}/courses/
  ADVANCED GET  /api/teachers/{id}/workload/

Courses
  EASY     GET  /api/courses/by-type/?type=online
  MEDIUM   GET  /api/courses/{id}/enrolled-students/
  ADVANCED POST /api/courses/{id}/enroll/
  ADVANCED GET  /api/courses/{id}/stats/
  ADVANCED GET  /api/courses/with-enrollment/                (annotate)
  ADVANCED GET  /api/courses/popular/?min=10                 (annotate + HAVING)
  ADVANCED POST /api/courses/bump-capacity/                  (F() update)

Grades
  EASY     GET  /api/grades/high-scores/
  MEDIUM   GET  /api/grades/by-course/?course_id=1
  ADVANCED GET  /api/grades/course-average/?course_id=1
  ADVANCED GET  /api/grades/near-max/?ratio=0.8              (F() filter)
  ADVANCED GET  /api/grades/statistics/?course_id=1          (aggregates)
  ADVANCED POST /api/grades/bulk-create/                     (bulk_create)
  ADVANCED POST /api/grades/bulk-update/                     (bulk_update)

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
