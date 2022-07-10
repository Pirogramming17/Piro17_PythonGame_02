from Gm import GameManager

class Game:
    def __init__(self) -> None:
        self.game = GameManager()

console = Game()
console.game.play()