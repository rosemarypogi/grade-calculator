def parse_grades(raw_grades: str) -> list[float]:
    """Parse comma-separated grades and ensure each is between 0 and 100."""
    entries = [entry.strip() for entry in raw_grades.split(",")]

    if not raw_grades.strip() or any(not entry for entry in entries):
        raise ValueError("Enter one or more grades separated by commas.")

    try:
        grades = [float(entry) for entry in entries]
    except ValueError as error:
        raise ValueError("Grades must be numbers.") from error

    if any(grade < 0 or grade > 100 for grade in grades):
        raise ValueError("Each grade must be between 0 and 100.")

    return grades


def main() -> None:
    raw_grades = input("Enter grades from 0 to 100, separated by commas: ")

    try:
        grades = parse_grades(raw_grades)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return

    average = sum(grades) / len(grades)
    print(f"Average grade: {average:.2f}")


if __name__ == "__main__":
    main()
