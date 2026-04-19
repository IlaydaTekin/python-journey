import unittest
from grade_tools import grade_note, average_grades, max_note, min_note, pass_notes, fail_notes

class TestGrades(unittest.TestCase):

    def test_grade_liste_not(self):
        self.assertEqual(grade_note("70?,85,90"), [70, 85, 90])

    def test_average_grade(self):
        self.assertEqual(average_grades("70,80,90"), 80.0)

    def test_maximum_grade(self):
        self.assertEqual(max_note("70,80,90"), 90)

    def test_minimum_grade(self):
        self.assertEqual(min_note("70,80,90"), 70)

    def test_passed_grades(self):
        self.assertEqual(pass_notes("30,50,70"), [70])

    def test_failed_grades(self):
        self.assertEqual(fail_notes("30,50,70"), [30, 50])

if __name__ == "__main__":
    unittest.main()