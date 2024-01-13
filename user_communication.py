from player import player

def communication_0():
    message = [
        "Hallo user, ich bin Dein persönlicher Assistent.",
        "Verrätst Du mir Deinen Vornamen?            ",  # Leerzeichen für kurze Pause bei der Ausgabe
        "Bitte antworte mit 'ja' oder 'nein'.",
    ]
    new_input = True
    # message = [
    #     "Hallo user, ich bin Dein persönlicher Assistent. Verrätst Du mir Deinen Vornamen?",
    #     "Schreibe einfach ja oder nein"
    # ],
    # new_input = True
    return message, new_input,


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

def communication_2(player_name: str) -> any:
    player.name = player_name.strip().capitalize()
    message = [
        f"{player.name} ist ein sehr schöner Name!",
        "Er erinnert mich an jemanden den ich vor langer Zeit gekannt habe, Wie möchtest",
        f"Du angesprochen werden? A) Liebe, B) Lieber oder C) Liebes {player.name}",
    ]
    new_input = True
    return message, new_input


def communication_3(gender: str) -> any:
    if gender == "a":
        player.sex = "female"
        message = [f"Alles klar liebe {player.name}"]
    elif gender == "b":
        player.sex = "male"
        message = [f"Alles klar lieber {player.name}"]
    elif gender == "c":
        player.sex = "divers"
        message = [f"Alles klar liebes {player.name}"]
    else:
        communication_2(player.name)

    new_input = False

    return message, new_input


def create_message(input_text: str, communication_counter: int) -> any:
    text = input_text.strip().lower()
    if communication_counter == 0:
        message, new_input = communication_0()
    if communication_counter == 1:
        message, new_input = communication_1(text)
    if communication_counter == 2:
        message, new_input = communication_2(text)
    if communication_counter == 3:
        message, new_input = communication_3(text)

    return message, new_input
