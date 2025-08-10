from PIL import Image, ImageDraw, ImageFont
import os

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_PATH = os.path.join(ASSETS_PATH, "RobotoSlab[wght].ttf")

class BoardRenderer:
    def __init__(self, board, size=300):       
        """
        board: lista de 9 elementos con "X", "O" o " "
        size: tamaño de la imagen (pixeles, cuadrada)
        """
        self.board = board
        self.size = size
        self.cell_size = size // 3
        self.font = ImageFont.truetype(FONT_PATH, self.cell_size - 20)

    def render(self, save_path=None):
        """
        Crea la imagen del tablero y la guarda si save_path se indica.
        Retorna el objeto Image.
        """
        img = Image.new("RGBA", (self.size, self.size), "white")
        draw = ImageDraw.Draw(img)

        # Dibujar líneas de la cuadrícula
        line_color = (50, 50, 50)
        line_width = 4
        for i in range(1, 3):
            # Líneas verticales
            draw.line([(i * self.cell_size, 0), (i * self.cell_size, self.size)], fill=line_color, width=line_width)
            # Líneas horizontales
            draw.line([(0, i * self.cell_size), (self.size, i * self.cell_size)], fill=line_color, width=line_width)

        # Dibujar X y O
        for i, cell in enumerate(self.board):
            if cell != " ":
                x = (i % 3) * self.cell_size + self.cell_size // 2
                y = (i // 3) * self.cell_size + self.cell_size // 2
                color = (200, 30, 30) if cell == "X" else (30, 30, 200)
                bbox = draw.textbbox((0, 0), cell, font=self.font)
                w = bbox[2] - bbox[0]
                h = bbox[3] - bbox[1]
                draw.text((x - w//2, y - h//2), cell, font=self.font, fill=color)


        if save_path:
            img.save(save_path)
        return img