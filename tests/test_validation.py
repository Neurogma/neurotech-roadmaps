import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path
import unittest

import scripts.validate as validate


ROOT = Path(__file__).resolve().parents[1]


class RepositoryChecksTest(unittest.TestCase):
    def run_command(self, *args):
        result = subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stdout + result.stderr,
        )

    def test_generated_markdown_is_current(self):
        self.run_command(
            "scripts/generate_roadmaps.py",
            "--check",
        )

    def test_structural_validation_passes(self):
        self.run_command(
            "scripts/validate.py",
            "--strict-provenance",
        )

    def test_stale_provenance_is_detected(self):
        stale_date = (
            date.today() - timedelta(days=31)
        ).isoformat()

        resources = {
            "example": {
                "status": "active",
                "provenance": {
                    "source_type": "official-project",
                    "last_verified": stale_date,
                    "review_interval_days": 30,
                },
            }
        }

        with self.assertRaises(AssertionError):
            validate.check_resource_provenance(
                resources,
                strict=True,
            )

    def test_non_active_resource_reference_is_rejected(self):
        records = {
            "node-a": (
                ROOT / "nodes" / "fake.yml",
                {"resources": ["resource-a"]},
            )
        }
        resources = {
            "resource-a": {
                "status": "needs-review",
            }
        }

        with self.assertRaises(AssertionError):
            validate.check_active_resources(
                records,
                resources,
            )


if __name__ == "__main__":
    unittest.main()
