from typing import List, Tuple, Dict


def get_knowledge_gaps(topics: str) -> List[int]:
    student_gaps = []
    for index, topic in enumerate(topics):
        if topic == '0':
            student_gaps.append(index)
    return sorted(student_gaps)


def get_unique_students(topics: List[str]) -> Tuple[Dict[str, int], List[str], Dict[str, List[int]]]:
    student_count = {}
    gaps = {}
    for student in topics:
        current_student_count = student_count.get(student, 0)
        student_count[student] = student_count[student] = current_student_count + 1
        gaps[student] = get_knowledge_gaps(student)
    unique_students = list(student_count.keys())
    return student_count, unique_students, gaps


def compute_team_points(first_student: List[int], second_student: List[int], team_points) -> int:
    team_points = team_points
    i, j = 0, 0
    while i < len(first_student) and j < len(second_student):
        if first_student[i] < second_student[j]:
            i += 1
        elif first_student[i] > second_student[j]:
            j += 1
        else:
            team_points -= 1
            i += 1
            j += 1
    return team_points


def acm_team(topic: List[str]):
    frequency_count = {}
    student_count, unique_students, knowledge_gaps = get_unique_students(topic)
    number_unique_students = len(unique_students)
    for i in range(number_unique_students - 1):
        first_student = knowledge_gaps[unique_students[i]]
        for j in range(i + 1, number_unique_students):
            second_student = knowledge_gaps[unique_students[j]]
            team_points = compute_team_points(first_student, second_student, len(unique_students[0]))
            current_frequency = frequency_count.get(team_points, 0)
            first_student_frequency = student_count[unique_students[i]]
            second_student_frequency = student_count[unique_students[j]]
            frequency_count[team_points] = current_frequency + (first_student_frequency * second_student_frequency)
    sorted_count = sorted(frequency_count.items(), key=lambda x: x[0], reverse=True)
    return sorted_count[0][0], sorted_count[0][1]
