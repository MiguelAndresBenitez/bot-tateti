class TatetiGame:
    
    def __init__(self):
        """Inicializa un nuevo juego con un tablero vacío y sin ganador."""
        self.board = [" " for _ in range(9)] # Tablero 3x3 representado como lista
        self.current_player = "X" # Jugador humano comienza (puede cambiarse)
        self.winner = None
        self.finished = False

    def reset(self):
        """Reinicia el juego a estado inicial."""
        self.__init__()
    
    def play(self, pos):
        if self.finished or self.board[pos] != " ":
            return False
        
        self.board[pos] = self.current_player
        if self.check_winner(self.current_player):
            self.winner = self.current_player
            self.finished = True
        elif " " not in self.board:
            self.finished = True  # Empate
        else:
            self.toggle_player()
        return True

    def toggle_player(self):
        """Cambia al siguiente jugador."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def available_moves(self):
        """Devuelve una lista con los índices de las casillas vacías."""
        return [i for i, cell in enumerate(self.board) if cell == " "]
    
    def check_winner(self, player):
        """Verifica si el jugador actual ha ganado."""
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
            [0, 4, 8], [2, 4, 6]              # Diagonales
        ]
        for combo in win_positions:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def get_board(self):
        """Devuelve una copia del tablero actual."""
        return self.board[:]