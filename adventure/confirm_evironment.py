import random


def confirm_environment(Environment, event_name, expected_text, choices, random_ints=None):

    actual_text = ""

    def mock_print(*args, **kwargs):
        nonlocal actual_text
        actual_text += " ".join(args) # + "\n"

    def mock_prompt(prompt_text, *args, **kwargs):
        nonlocal actual_text
        simulated_choice = choices.pop(0)
        actual_text += "\n" + prompt_text + ": " + simulated_choice + "\n"
        return simulated_choice

    def mock_randint(*args, **kwargs):
        return random_ints.pop(0)

    # creating a temporary mock randint function
    real_randint = random.randint
    random.randint = mock_randint

    # creating an instance of a mock environment
    environment = Environment(mock_print, mock_prompt)

    # getting the environment function and invoking it after
    event_function = getattr(environment, event_name)
    event_function()

    # setting random.randint back to default working conditions
    random.randint = real_randint

    # This is where we are comparing the two string outputs and comparing them.
    # White space is needing to be removed in order to compare accurately,
    # which is taken care of by '.strip().split("\n")'
    print(f"ACTUAL: \n {actual_text}")
    print(f"EXPECTED: \n {expected_text}")
    actual_lines = actual_text.strip().split("\n")
    # print(f"ACTUAL: \n {actual_lines}")
    expected_lines = expected_text.strip().split("\n")
    # print(f"Expected: \n {expected_lines}")


    assert len(actual_lines) == len(expected_lines), len(expected_lines)

    for actual_line, expected_line in zip(actual_lines, expected_lines):
        assert actual_line.strip() == expected_line.strip(), f"ACTUAL: {actual_line} --- EXPECTED: {expected_line}"
