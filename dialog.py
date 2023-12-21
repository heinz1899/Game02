def create_message(input_text=None):
    """_summary_

    Args:
        input_text: Defaults to None.

    Returns:
        message, new_input (True if user-input is expected)

    """
    new_input: bool = False
    if input_text == "ja":
        message = "Du hast ja gesagt :-)"
        new_input = True
    elif input_text == "nein":
        message = "Du hast nein gesagt :-("
        new_input = False

    return message, new_input
