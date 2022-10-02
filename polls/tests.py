from io import StringIO

from django.core.management import call_command
from django.test import TestCase


class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command("closepoll", poll_ids=1, stdout=out)
        self.assertIn("Expected output", out.getvalue())
