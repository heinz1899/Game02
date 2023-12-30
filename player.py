class Character:
    def __init__(self, name: str = "user", sex: str = "divers") -> None:
        self.name = name
        self.sex = sex
        self.prompt = f"{self.name}>: "

player = Character()
