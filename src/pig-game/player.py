class Player:
    """Represents a player and their accumulated score."""
    def __init__(self, index: int):
        self.index = index
        self.score = 0

    def __repr__(self):
        return f"Player({self.index}, score={self.score})"
