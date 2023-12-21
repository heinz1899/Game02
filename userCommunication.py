def level_1(text):
    message = ""
    if text == "ja":
        message = "Vielen Dank! Bitte gib Deinen Vornamen in das Textfeld ein"
        new_input = True
    elif text == "nein":
        message = "Das kann ich gut verstehen. Ich werde Dich einfach 'User' nennen.\n Wenn Du möchtest können wir jetzt weiter machen."
        new_input = False
    else:
        message = "Ich habe Dich nicht verstanden."
        new_input = True

    return message, new_input


def create_message(input_text, level):
    text = input_text.lower()
    """Processes user input \n
    Args:
        input_text: Defaults to None.
    Returns:
        message, new_input (True if user-input is expected)
    """
    if level == 1:
        message, new_input = level_1(text)

    return message, new_input
