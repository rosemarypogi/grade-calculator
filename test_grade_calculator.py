import unittest

from grade_calculator import parse_grades


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

    def test_rejects_missing_grade_between_commas(self):
        with self.assertRaises(ValueError):
            parse_grades("80, , 90")


if __name__ == "__main__":
    unittest.main()
