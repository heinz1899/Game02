def communication_0():
    message = ["Hallo user, ich bin Dein persönlicher Assistent.", "Verrätst Du mir Deinen Vornamen?", ""]
    new_input = True
    # message = [
    #     "Hallo user, ich bin Dein persönlicher Assistent. Verrätst Du mir Deinen Vornamen?",
    #     "Schreibe einfach ja oder nein"
    # ],
    # new_input = True
    return message, new_input


def communication_1(input_text):
    if input_text == "ja":
        message = ["Vielen Dank! Bitte gib Deinen Vornamen in das Textfeld ein.", ""]
        new_input = True
    elif input_text == "nein":
        message = ['Das kann ich gut verstehen.', 'Ich werde Dich einfach "user" nennen.']
        new_input = False
    else:
        message = ["Ich habe Dich nicht verstanden.", "Bitte antworte mit 'Ja' oder 'Nein'."]
        new_input = True

    return message, new_input


def create_message(input_text: str, level: int):
    text = input_text.strip().lower()
    if level == 0:
        message, new_input = communication_0()
    if level == 1:
        message, new_input = communication_1(text)

    return message, new_input
