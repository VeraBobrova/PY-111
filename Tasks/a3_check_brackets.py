def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    sequence = []
    brackets = {"(": ")"}

    for i in brackets_row:
        if i in brackets:
            sequence.append(brackets[i])
        elif not sequence or i != sequence.pop():
            return False
    return not sequence
