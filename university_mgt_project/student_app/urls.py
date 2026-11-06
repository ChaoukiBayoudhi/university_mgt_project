from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet,TeacherViewSet,CourseViewSet,GradeViewSet,ProfileViewSet,InscriptionViewSet
router=routers.DefaultRouter()
router.register(r'students',StudentViewSet)
router.register(r'teachers',TeacherViewSet)
router.register(r'courses',CourseViewSet)
router.register(r'grades',GradeViewSet)
router.register(r'profiles',ProfileViewSet)
router.register(r'inscriptions',InscriptionViewSet)

urlpatterns=[
    path('', include(router.urls))
]
