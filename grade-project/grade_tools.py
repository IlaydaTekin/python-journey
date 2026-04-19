#grade_tools.py

def grade_note(text):
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(".", "")

    parts = text.split(",")
    grades = []

    for p in parts:
        p = p.strip()
        if p != "":
            grades.append(int(p))

    return grades


def average_grades(text):
    grades = grade_note(text)
    total = 0

    for i in grades:
        total += i

    return total / len(grades)


def max_note(text):
    grades = grade_note(text)
    return max(grades)


def min_note(text):
    grades = grade_note(text)
    return min(grades)


def pass_notes(text):
    grades = grade_note(text)
    passed = []

    for i in grades:
        if i > 50:
            passed.append(i)

    return passed


def fail_notes(text):
    grades = grade_note(text)
    failed = []

    for i in grades:
        if i <= 50:
            failed.append(i)

    return failed


def grade_summary(text):
    return {
        "grades": grade_note(text),
        "average grade": average_grades(text),
        "the highest grade": max_note(text),
        "the lowest grade": min_note(text),
        "passed": pass_notes(text),
        "failed": fail_notes(text)
    }

