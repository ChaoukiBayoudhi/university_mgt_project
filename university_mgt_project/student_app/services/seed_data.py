"""
FakeDataService — insert realistic Tunisian demo data into the database.

Latin names go into name/familyName (English alphabetic).
Arabic names are stored in bio/headline for bilingual demos.
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from datetime import date, timedelta
from decimal import Decimal

from django.db import transaction
from django.utils import timezone

from student_app.enumerations import (
    AcademicLevel,
    CourseType,
    Gender,
    GradeName,
    InscriptionStatus,
    Semester,
    TeacherRank,
)
from student_app.models import Course, Grade, Inscription, Profile, Student, Teacher
from student_app.services.tunisian_names import (
    COURSE_CATALOG,
    DEPARTMENTS,
    TUNISIAN_CITIES,
    TUNISIAN_PEOPLE,
)


@dataclass
class SeedResult:
    teachers: int = 0
    students: int = 0
    courses: int = 0
    profiles: int = 0
    inscriptions: int = 0
    grades: int = 0
    cleared: bool = False
    details: list[str] = field(default_factory=list)


class FakeDataService:
    """Generate and persist fake university data (Tunisian context)."""

    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    @transaction.atomic
    def seed(
        self,
        *,
        n_teachers: int = 6,
        n_students: int = 18,
        clear: bool = False,
    ) -> SeedResult:
        result = SeedResult()

        if clear:
            self.clear_all()
            result.cleared = True
            result.details.append("Cleared Grade, Inscription, Profile, Course, Student, Teacher.")

        people = list(TUNISIAN_PEOPLE)
        self.rng.shuffle(people)

        teachers = self._create_teachers(people[:n_teachers], result)
        students = self._create_students(people[n_teachers : n_teachers + n_students], result)
        courses = self._create_courses(teachers, result)
        self._create_profiles(students, teachers, result)
        self._create_inscriptions_and_grades(students, courses, result)

        result.details.append(
            f"Seeded teachers={result.teachers}, students={result.students}, "
            f"courses={result.courses}, profiles={result.profiles}, "
            f"inscriptions={result.inscriptions}, grades={result.grades}."
        )
        return result

    def clear_all(self) -> None:
        # Order matters because of FKs / composite PKs
        Grade.objects.all().delete()
        Inscription.objects.all().delete()
        Profile.objects.all().delete()
        Course.objects.all().delete()
        Student.objects.all().delete()
        Teacher.objects.all().delete()

    # ------------------------------------------------------------------
    # creators
    # ------------------------------------------------------------------

    def _create_teachers(self, people, result: SeedResult) -> list[Teacher]:
        teachers: list[Teacher] = []
        ranks = list(TeacherRank)
        for index, (first, family, ar_first, ar_family, gender) in enumerate(people):
            dept_en, dept_ar = DEPARTMENTS[index % len(DEPARTMENTS)]
            city_en, city_ar = TUNISIAN_CITIES[index % len(TUNISIAN_CITIES)]
            email = f"{first.lower()}.{family.lower().replace(' ', '')}@isg.u-tunis.tn"
            email = email.replace("'", "")
            teacher, created = Teacher.objects.get_or_create(
                email=email,
                defaults={
                    "name": first,
                    "familyName": family,
                    "phone": f"+2169{self.rng.randint(1000000, 9999999)}",
                    "department": dept_en,
                    "specialty": dept_en,
                    "rank": ranks[index % len(ranks)].value,
                    "bio": (
                        f"الاسم بالعربية: {ar_first} {ar_family}. "
                        f"أستاذ(ة) بقسم {dept_ar}، مقيم(ة) بـ {city_ar} ({city_en})."
                    ),
                    "hiredAt": date(2015 + (index % 8), 9, 1),
                    "isActive": True,
                },
            )
            if created:
                result.teachers += 1
            teachers.append(teacher)
        return teachers

    def _create_students(self, people, result: SeedResult) -> list[Student]:
        students: list[Student] = []
        levels = list(AcademicLevel)
        # Keep clear of existing demo PKs if any remain
        base_inscription = 20260001
        for index, (first, family, ar_first, ar_family, gender) in enumerate(people):
            city_en, city_ar = TUNISIAN_CITIES[index % len(TUNISIAN_CITIES)]
            inscription = base_inscription + index
            cin = f"{self.rng.randint(10000000, 99999999)}"
            email = f"{first.lower()}.{family.lower().replace(' ', '')}{index}@etudiant.isg.tn"
            email = email.replace("'", "")
            student, created = Student.objects.get_or_create(
                inscriptionNumber=inscription,
                defaults={
                    "cin": cin,
                    "name": first,
                    "familyName": family,
                    "email": email,
                    "phone": f"+2162{self.rng.randint(1000000, 9999999)}",
                    "address": f"{self.rng.randint(1, 120)} Av. Habib Bourguiba, {city_en}",
                    "gender": Gender.MALE if gender == "M" else Gender.FEMALE,
                    "level": levels[index % len(levels)].value,
                    "bio": (
                        f"الاسم بالعربية: {ar_first} {ar_family}. "
                        f"طالب(ة) من {city_ar}."
                    ),
                    "birthday": date(2002 + (index % 5), self.rng.randint(1, 12), self.rng.randint(1, 28)),
                    "isActive": True,
                },
            )
            if created:
                result.students += 1
            students.append(student)
        return students

    def _create_courses(self, teachers: list[Teacher], result: SeedResult) -> list[Course]:
        courses: list[Course] = []
        types = list(CourseType)
        semesters = [Semester.S1, Semester.S2]
        for index, (code, title_en, title_ar) in enumerate(COURSE_CATALOG):
            teacher = teachers[index % len(teachers)] if teachers else None
            end = timezone.now() + timedelta(days=90 + 10 * index)
            course, created = Course.objects.get_or_create(
                code=code,
                defaults={
                    "title": title_en,
                    "endDate": end,
                    "durationByWeek": timedelta(hours=3),
                    "credits": 3 + (index % 4),
                    "semester": semesters[index % 2].value,
                    "maxStudents": 40,
                    "room": f"A{100 + index}",
                    "description": f"{title_en} / {title_ar}",
                    "type": types[index % len(types)].value,
                    "isActive": True,
                    "teacher": teacher,
                },
            )
            if created:
                result.courses += 1
            courses.append(course)
        return courses

    def _create_profiles(
        self,
        students: list[Student],
        teachers: list[Teacher],
        result: SeedResult,
    ) -> None:
        for student in students:
            first = student.name
            family = student.familyName
            slug = f"{first.lower()}{family.lower().replace(' ', '')}"
            # Extract Arabic name from bio if present
            arabic_bit = student.bio.split(".")[0] if student.bio else first
            _, created = Profile.objects.get_or_create(
                student=student,
                defaults={
                    "headline": f"{arabic_bit} | ISG Tunis student",
                    "skills": "Python, Django, SQL, Git",
                    "github": f"https://github.com/{slug}",
                    "linkedin": f"https://www.linkedin.com/in/{slug}",
                    "website": f"https://{slug}.example.tn",
                },
            )
            if created:
                result.profiles += 1

        for teacher in teachers:
            slug = f"{teacher.name.lower()}{teacher.familyName.lower().replace(' ', '')}"
            arabic_bit = teacher.bio.split(".")[0] if teacher.bio else teacher.name
            _, created = Profile.objects.get_or_create(
                teacher=teacher,
                defaults={
                    "headline": f"{arabic_bit} | {teacher.department}",
                    "skills": "Teaching, Research, Mentoring",
                    "github": f"https://github.com/{slug}",
                    "website": f"https://isg.u-tunis.tn/~{slug}",
                },
            )
            if created:
                result.profiles += 1

    def _create_inscriptions_and_grades(
        self,
        students: list[Student],
        courses: list[Course],
        result: SeedResult,
    ) -> None:
        if not students or not courses:
            return

        situations = [
            InscriptionStatus.ACCEPTED,
            InscriptionStatus.ACCEPTED,
            InscriptionStatus.PENDING,
            InscriptionStatus.COMPLETED,
        ]
        grade_kinds = [GradeName.EXAM, GradeName.PROJECT, GradeName.QUIZ]

        for student in students:
            # Each student joins 2–4 courses
            chosen = self.rng.sample(courses, k=min(len(courses), self.rng.randint(2, 4)))
            for course in chosen:
                situation = self.rng.choice(situations).value
                inscription, created = Inscription.objects.get_or_create(
                    student=student,
                    course=course,
                    defaults={
                        "situation": situation,
                        "remark": "تسجيل تجريبي / demo inscription",
                        "finalAverage": None,
                    },
                )
                if created:
                    result.inscriptions += 1

                if situation not in (
                    InscriptionStatus.ACCEPTED,
                    InscriptionStatus.COMPLETED,
                ):
                    continue

                weighted = Decimal("0")
                coeff_sum = Decimal("0")
                for grade_name in grade_kinds:
                    mark = Decimal(str(round(self.rng.uniform(8, 19.5), 2)))
                    coeff = Decimal("1.0") if grade_name != GradeName.EXAM else Decimal("2.0")
                    grade, g_created = Grade.objects.get_or_create(
                        student=student,
                        course=course,
                        gradeName=grade_name.value,
                        defaults={
                            "mark": mark,
                            "maxMark": Decimal("20"),
                            "coefficient": float(coeff),
                            "justification": "Note مولّدة آلياً / auto-generated mark",
                        },
                    )
                    if g_created:
                        result.grades += 1
                        weighted += mark * coeff
                        coeff_sum += coeff
                    else:
                        weighted += Decimal(str(grade.mark)) * Decimal(str(grade.coefficient))
                        coeff_sum += Decimal(str(grade.coefficient))

                if coeff_sum > 0 and inscription.finalAverage is None:
                    inscription.finalAverage = (weighted / coeff_sum).quantize(Decimal("0.01"))
                    inscription.save(update_fields=["finalAverage", "updatedAt"])
