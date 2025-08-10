from utils.board_renderer import BoardRenderer

def main():
    # Ejemplo de tablero
    board = [
        "X", "O", "X",
        " ", "O", " ",
        " ", " ", "X"
    ]

    renderer = BoardRenderer(board)
    img = renderer.render("tablero_test.png")
    img.show()  # Esto abre la imagen con el visor predeterminado de tu SO

if __name__ == "__main__":
    main()
