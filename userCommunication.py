from typing import Union


def level_1(text):
    if text == "ja":
        message = ["Vielen Dank! Bitte gib Deinen Vornamen in das Textfeld ein.", ""]
        new_input = True
    elif text == "nein":
        message = ['Das kann ich gut verstehen.', 'Wenn Du möchtest können wir jetzt weiter machen... ']
        new_input = False
    else:
        message = ["Ich habe Dich nicht verstanden.", "Bitte antworte mit 'Ja' oder 'Nein'."]
        new_input = True

    return message, new_input


def create_message(input_text: str, level: int = 1) -> str:
    """Processes user input

    Args:
        input_text (_type_): _description_
        level (_type_): _description_

    Returns:
        message, new_input: _description_
    """
    text = input_text.lower()
    if level == 1:
        message = level_1(text)

    return message
