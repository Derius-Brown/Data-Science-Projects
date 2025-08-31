import sys

grades = {
    'Biology': 80,
    'Physics': 88,
    'Chemistry': 98,
    'Math': 89,
    'English': 79,
    'Music': 67,
    'History': 68,
    'Art': 53,
    'Economics': 95,
    'Psychology': 88
}

if len(sys.argv) > 1:
    exclude_subject = sys.argv[1]
    total = sum(score for subject, score in grades.items() if subject != exclude_subject)
    count = len(grades) - 1
    average = total / count
    print(f"{average:.2f}")
