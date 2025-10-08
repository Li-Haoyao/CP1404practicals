"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly formatted report."""
    subjects = load_subject_data(FILENAME)
    display_subjects(subjects)


def load_subject_data(filename=FILENAME):
    """Read subject data from file into a list of [subject_code, lecturer, student_count]."""
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subjects(subjects):
    """Display subject details in formatted style."""
    for subject in subjects:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()
