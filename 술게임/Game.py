from Gm import GameManager

class Game:
    def __init__(self) -> None:
        self.game = GameManager()

game = Game()
game.game.play()