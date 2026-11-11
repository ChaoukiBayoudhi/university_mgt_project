"""
Generate Tunisian/Arabic fake data and insert it via FakeDataService.

Usage:
  pipenv run python manage.py seed_fake_data
  pipenv run python manage.py seed_fake_data --clear --students 18 --teachers 6
"""

from django.core.management.base import BaseCommand

from student_app.services import FakeDataService


class Command(BaseCommand):
    help = "Seed the database with Tunisian Latin + Arabic fake university data."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing student_app rows before seeding.",
        )
        parser.add_argument("--teachers", type=int, default=6)
        parser.add_argument("--students", type=int, default=18)
        parser.add_argument("--seed", type=int, default=42, help="RNG seed for reproducibility.")

    def handle(self, *args, **options):
        service = FakeDataService(seed=options["seed"])
        result = service.seed(
            n_teachers=options["teachers"],
            n_students=options["students"],
            clear=options["clear"],
        )
        for line in result.details:
            self.stdout.write(self.style.SUCCESS(line))
        self.stdout.write(
            self.style.NOTICE(
                "Names use English alphabetic Tunisian forms in name/familyName; "
                "Arabic forms are in bio/headline."
            )
        )
