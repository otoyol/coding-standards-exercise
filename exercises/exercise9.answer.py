def add_numbers(first_number, second_number):
    """
    Adds two numbers together and returns the result.

    Args:
    first_number (int): The first number.
    second_number (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return first_number + second_number


def calculate_percentage(value, total):
    """
    Calculates the percentage of value in relation to total.

    Args:
    value (int): The first number.
    total (int): The total of the two numbers.

    Returns:
    float: The percentage of value in relation to total.
    """
    return (value * 100) / total


if __name__ == "__main__":
    total = add_numbers(5, 7)

    percentage = calculate_percentage(5, total)

    print('Argument one percentage is: ', percentage)
