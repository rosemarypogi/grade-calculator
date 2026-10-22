from contextlib import redirect_stdout
from io import StringIO
import unittest
from unittest.mock import patch

from grade_calculator import calculate_average, main, parse_grades


class ParseGradesTests(unittest.TestCase):
    def test_parses_comma_separated_grades(self):
        self.assertEqual(parse_grades("80, 90, 78.5"), [80.0, 90.0, 78.5])

    def test_rejects_empty_input(self):
        with self.assertRaises(ValueError):
            parse_grades(" ")

    def test_rejects_non_numeric_grade(self):
        with self.assertRaises(ValueError):
            parse_grades("80, A")

    def test_rejects_grade_outside_allowed_range(self):
        for raw_grades in ("-1", "101"):
            with self.subTest(raw_grades=raw_grades):
                with self.assertRaises(ValueError):
                    parse_grades(raw_grades)


class CalculateAverageTests(unittest.TestCase):
    def test_calculates_average(self):
        self.assertEqual(calculate_average([80.0, 90.0, 70.0]), 80.0)

    def test_rejects_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_average([])


class MainTests(unittest.TestCase):
    def test_displays_grade_summary(self):
        output = StringIO()
        with patch("builtins.input", return_value="80, 90, 70"):
            with redirect_stdout(output):
                main()

        self.assertIn("Grades entered: 3", output.getvalue())
        self.assertIn("Lowest grade: 70.00", output.getvalue())
        self.assertIn("Highest grade: 90.00", output.getvalue())
        self.assertIn("Average grade: 80.00", output.getvalue())

    def test_rejects_missing_grade_between_commas(self):
        with self.assertRaises(ValueError):
            parse_grades("80, , 90")


if __name__ == "__main__":
    unittest.main()
