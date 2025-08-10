from models.tateti_game import TatetiGame
from IA.AI.basic_IA import MinimaxAI

class GameController:
    def __init__(self):
        """Inicializa la lógica del juego y la IA."""
        self.game = TatetiGame()
        self.ai = MinimaxAI(self.game)

    def player_move(self, pos):
        """
        Intenta hacer la jugada del jugador humano.
        Retorna True si fue válida, False si no.
        """
        return self.game.play(pos)

    def ai_move(self):
        """
        La IA calcula y realiza su mejor movimiento.
        Retorna la posición jugada o None si no hay movimientos.
        """
        if self.game.finished:
            return None

        move = self.ai.get_best_move()
        if move is not None:
            self.game.play(move)
        return move

    def is_finished(self):
        """Retorna True si el juego terminó (ganador o empate)."""
        return self.game.finished

    def get_winner(self):
        """Retorna el ganador ("X", "O" o None)."""
        return self.game.winner

    def get_board(self):
        """Retorna una copia del tablero actual."""
        return self.game.get_board()

    def reset_game(self):
        """Reinicia el juego."""
        self.game.reset()
