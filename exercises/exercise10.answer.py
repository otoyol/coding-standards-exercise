def get_score_percentage(score, total):
    """
    Calculates the percentage score of a given score out of a total.

    Args:
    score (float): The score achieved.
    total (float): The total score available.

    Returns:
    float: The percentage score achieved.
    """
    return (score * 100) / total


if __name__ == "__main__":
    # Calculate student score percentage
    student_score = 45
    student_total = 60
    student_percentage = get_score_percentage(student_score, student_total)
    print('Student score percentage:', student_percentage)

    # Calculate teacher score percentage
    teacher_score = 75
    teacher_total = 150
    teacher_percentage = get_score_percentage(teacher_score, teacher_total)
    print('Teacher score percentage:', teacher_percentage)
