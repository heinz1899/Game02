from player import player

def communication_0() -> tuple[str, bool]:
    message = [
        "Hallo user, ich bin Dein persönlicher Assistent.",
        "Verrätst Du mir Deinen Vornamen? (j/n)"
    ]
    new_input = True
    next_message = 1
    return message, new_input, next_message

def communication_1(input_text: str) -> tuple[str, bool, int]:
    if input_text == "j":
        message = ["Vielen Dank! Bitte gib Deinen Vornamen in das Textfeld ein.", ""]
        new_input = True
    elif input_text == "n":
        message = ['Das kann ich gut verstehen.', 'Ich werde Dich einfach "user" nennen.']
        new_input = False
    else:
        message = ["Ich habe Dich nicht verstanden.", "Bitte antworte mit 'j' oder 'n'."]
        new_input = True
    next_message = 2
    return (message, new_input, next_message)


def communication_2(player_name: str) -> tuple[str, bool]:
    player.name = player_name.strip().capitalize()
    message = [
        f"{player.name} ist ein sehr schöner Name!",
        "Er erinnert mich an jemanden den ich vor langer Zeit gekannt habe, Wie möchtest",
        f"Du angesprochen werden? A) Liebe, B) Lieber oder C) Liebes {player.name}",
    ]
    next_message = 3
    new_input = True
    return message, new_input, next_message


def communication_3(gender: str) -> tuple[str, bool, int]:
    new_input = True
    next_message = None
    if gender == "a":
        player.sex = "female"
        message = [f"Alles klar liebe {player.name}."]
        next_message = 4
    elif gender == "b":
        player.sex = "male"
        message = [f"Alles klar lieber {player.name}."]
        next_message = 4
    elif gender == "c":
        player.sex = "divers"
        message = [f"Alles klar liebes {player.name}."]
        next_message = 4
    else:
        message = [
            f"Gib A für Liebe {player.name}, B für Lieber {player.name}",
            f"oder C für Liebes {player.name} ein."
        ]
        next_message = 3
        new_input = True

    return message, new_input, next_message

def communication_4():
    new_input = False
    next_message = None
    message = ["Lass die Spiele beginnen!"]

    return message, new_input, next_message



def create_message(input_text: str, communication_counter: int) -> tuple[str, bool]:
    text = input_text.strip().lower()
    # Begrüßung
    if communication_counter == 0:
        message, new_input, next_message = communication_0()
    # Namen eingeben ja/nein
    if communication_counter == 1:
        message, new_input, next_message = communication_1(text)
    # Abfrage Name oder "user"
    if communication_counter == 2:
        message, new_input, next_message = communication_2(text)
    # Abfrage gender
    if communication_counter == 3:
        message, new_input, next_message = communication_3(text)
    if communication_counter == 4:
        message, new_input, next_message = communication_3(text)

    return message, new_input, next_message
