"""
Player wird in der user_communiction und in der main verwendet.
Um Zirkelschlüsse zu vermeiden, erfolgt die Auslagerung in eine separate Datei
"""


class Character:
    def __init__(self, name: str, sex: str, human: bool = True) -> None:
        self.human = human
        self.name = name
        self.sex = sex
        self.prompt = f"{self.name}>: "
        self.game_result = []


player = Character("Heiner", "divers", human=True)  # der Mensch, der das spiel spielt
