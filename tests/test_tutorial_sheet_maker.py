import unittest

from tutorial_sheet_maker import SYSTEM_PROMPT, prepare_tutorial_sheet


class TutorialSheetMakerTests(unittest.TestCase):
    def test_prepare_tutorial_sheet_includes_role_and_topics(self):
        sheet = prepare_tutorial_sheet("Calculus, Linear Algebra")
        self.assertIn(SYSTEM_PROMPT, sheet)
        self.assertIn("- Calculus", sheet)
        self.assertIn("- Linear Algebra", sheet)
        self.assertIn("### Topic 1: Calculus", sheet)
        self.assertIn("### Topic 2: Linear Algebra", sheet)

    def test_prepare_tutorial_sheet_requires_non_empty_syllabus(self):
        with self.assertRaisesRegex(ValueError, "at least one topic"):
            prepare_tutorial_sheet("   ")


if __name__ == "__main__":
    unittest.main()
