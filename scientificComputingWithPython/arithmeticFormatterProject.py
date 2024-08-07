def arithmetic_arranger(problems, show_answers=False):
    # check number of problems
    if has_too_many(problems):
        return 'Error: Too many problems.'

    # check for incorrect operators
    for problem in problems:
        if is_not_add_or_subtract(problem):
            return "Error: Operator must be '+' or '-'."

    # separate problems into their parts
    problems_in_parts = separate_problems_into_parts(problems)

    # check number length and only digits
    for problem in problems_in_parts:
        if is_number_too_long(problem['top']) or is_number_too_long(problem['bottom']):
            return 'Error: Numbers cannot be more than four digits.'
        if is_not_only_digits(problem['top']) or is_not_only_digits(problem['bottom']):
            return 'Error: Numbers must only contain digits.'

    # format output
    output = format_separated_problems(problems_in_parts, show_answers)

    return output

def has_too_many(problems):
    if len(problems) > 5:
        return True
    return False

def is_not_add_or_subtract(problem):
    if problem.find('-') != -1 or problem.find('+') != -1:
        return False
    return True

def is_not_only_digits(number):
    if not number.isdigit():
        return True
    return False

def is_number_too_long(number):
    if len(number) > 4:
        return True
    return False

def separate_problems_into_parts(problems):
    separated_problems = []
    for problem in problems:
        top, operator, bottom = problem.split()
        this_problem = {'top':top, 'bottom':bottom, 'operator':operator}
        separated_problems.append(this_problem)

    return separated_problems

def format_separated_problems(problems, show_answers):
    space = ' '
    top_line_output = ''
    bottom_line_output = ''
    answer_line_output = ''
    div_line = ''
    formatted_output = ''
    sum_with_strings = {'+': lambda top, bottom: int(top) + int(bottom),
                        '-': lambda top, bottom: int(top) - int(bottom)}

    for problem in problems:
        top_num = problem['top']
        bottom_num = problem['bottom']
        operator = problem['operator']
        length_diff = abs(len(top_num) - len(bottom_num))
        number_of_characters = 2 + max(len(top_num), len(bottom_num))

        # calculate number spacing
        if len(top_num) >= len(bottom_num):
            top_line_output += space * 2 + top_num
            bottom_line_output += operator + space + space * length_diff + bottom_num
        elif len(top_num) < len(bottom_num):
            top_line_output += space * (length_diff + 2) + top_num
            bottom_line_output += operator + space + bottom_num

        div_line += '-' * number_of_characters 

        # calculate answer and spacing
        answer = str(sum_with_strings[operator](top_num, bottom_num))
        answer_line_output += space * (number_of_characters - len(answer)) + answer

        # add trailing spaces
        top_line_output += space * 4
        bottom_line_output += space * 4
        div_line += space * 4
        answer_line_output += space * 4

    formatted_output += f"{top_line_output.rstrip(space)}\n{bottom_line_output.rstrip(space)}\n{div_line.rstrip(space)}"

    if show_answers:
        formatted_output += f"\n{answer_line_output.rstrip(space)}"

    return formatted_output

print(f'\n{arithmetic_arranger(["32 + 698", "32 + 698", "2 - 3801", "45 + 43", "1234 + 49"], True)}')