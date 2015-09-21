from django.core.management.base import BaseCommand
import os, sys

sys.path.append("../../..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from main.models import FridayTweet


class Command(BaseCommand):

    def handle(self, *args, **options):
        help = "Makes a new tweet for CmonSister."

        FridayTweet.bye_felicia()
