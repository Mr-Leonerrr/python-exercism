def round_scores(student_scores: list) -> list:
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.

    This function should consume the input list
    and return a new list with all the scores converted to ints.
    """

    return [round(score) for score in student_scores]


FAILURE = 40


def count_failed_students(student_scores: "list[int]") -> int:
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.

    This function should count up the number of students
    who don't have passing scores and return that count as an integer.
    A student needs a score greater than 40 to achieve
    a passing grade on the exam.
    """

    return len([score for score in student_scores if score <= FAILURE])


def above_threshold(student_scores: "list[int]", threshold: int) -> "list[int]":
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.

    This function should return a list of all scores that are >= to threshold.
    """

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> "list[int]":
    """
    :param highest: integer of highest exam score.
    :return: list of integer score thresholds for each F-A letter grades.

    This function takes the "highest" score on the exam as a parameter,
    and returns a list of lower score thresholds
    for each letter grade from "F" to "A".
    """

    step = (highest - FAILURE)/4
    return [int(41 + i * step) for i in range(4)]


def student_ranking(student_scores: "list[int]", student_names: "list[str]") -> "list[str]":
    """
     :param student_scores: list of scores in descending order.
     :param student_names: list of names in descending order by exam score.
     :return: list of strings in format ["<rank>. <student name>: <score>"].
     """

    return [f'{x + 1}. {student_names[x]}: {score}' for x, score in enumerate(student_scores)]


def perfect_score(student_info: "list[str, int]") -> str:
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: First [<student name>, 100] found OR "No perfect score."

    The function should return the first [<name>, <score>]
    pair of the student who scored 100 on the exam.
    """
    for student in student_info:
        if student[1] == 100:
            return student

    return "No perfect score."
