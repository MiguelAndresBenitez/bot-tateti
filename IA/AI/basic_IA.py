# ai/minimax_ai.py

class MinimaxAI:
    def __init__(self, game):
        """Recibe una instancia de TatetiGame."""
        self.game = game

    def minimax(self, board, is_maximizing):
        """
        Algoritmo Minimax recursivo.
        board: lista con el estado actual.
        is_maximizing: True si la IA está jugando (O), False si el jugador (X).
        """
        if self.game.check_winner("O"):
            return 1
        elif self.game.check_winner("X"):
            return -1
        elif " " not in board:
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for move in self.game.available_moves():
                board[move] = "O"
                score = self.minimax(board, False)
                board[move] = " "
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for move in self.game.available_moves():
                board[move] = "X"
                score = self.minimax(board, True)
                board[move] = " "
                best_score = min(score, best_score)
            return best_score

    def get_best_move(self):
        """Busca la mejor jugada para la IA (O)."""
        best_score = -float("inf")
        best_move = None
        for move in self.game.available_moves():
            self.game.board[move] = "O"
            score = self.minimax(self.game.board, False)
            self.game.board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move
        return best_move
