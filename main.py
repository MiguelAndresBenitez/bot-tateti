from controllers.game_controllers import GameController

def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---+---+---")
    print()

def main():
    game = GameController()
    print("¡Vamos a jugar Tatetí!")
    print("Vos sos X, la IA es O.")

    print_board(game.get_board())

    while not game.is_finished():
        valid_move = False
        while not valid_move:
            try:
                pos = int(input("Elegí posición (0-8): "))
                if pos not in range(9):
                    print("Número inválido, debe ser 0 a 8.")
                    continue
                valid_move = game.player_move(pos)
                if not valid_move:
                    print("Casilla ocupada o juego terminado, probá otra.")
            except ValueError:
                print("Debe ingresar un número válido.")

        print_board(game.get_board())

        if game.is_finished():
            break

        print("Turno de la IA...")
        ai_move = game.ai_move()
        print(f"IA jugó en posición {ai_move}")
        print_board(game.get_board())

    winner = game.get_winner()
    if winner == "X":
        print("¡Ganaste! 🎉")
    elif winner == "O":
        print("La IA ganó. Mejor suerte la próxima.")
    else:
        print("Empate!")

if __name__ == "__main__":
    main()