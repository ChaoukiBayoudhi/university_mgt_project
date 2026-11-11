#!/usr/bin/env python
"""
Standalone entry point to generate Tunisian/Arabic fake data.

Preferred (same logic):
  pipenv run python manage.py seed_fake_data --clear

This script also works:
  pipenv run python generate_fake_data.py --clear
"""

import argparse
import os
import sys

import django


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Seed Tunisian/Arabic fake university data."
    )
    parser.add_argument("--clear", action="store_true")
    parser.add_argument("--teachers", type=int, default=6)
    parser.add_argument("--students", type=int, default=18)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "university_mgt_project.settings")
    django.setup()

    from student_app.services import FakeDataService

    result = FakeDataService(seed=args.seed).seed(
        n_teachers=args.teachers,
        n_students=args.students,
        clear=args.clear,
    )
    for line in result.details:
        print(line)
    print("Done. Latin Tunisian names → name/familyName; Arabic names → bio/headline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
