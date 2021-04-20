from move import Move


class Character:
    def __init__(self, name):
        self.name = name
        self.moveset = []

    def add_move(self, move):
        self.moveset.append(move)

