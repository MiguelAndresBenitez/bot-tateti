import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from .game_controllers import GameController
from utils.board_renderer import BoardRenderer

# Configurar el logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self.game_controller = {} # Diccionario para manejar múltiples juegos por chat_id
        
        # Añadir handlers
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("reset", self.reset_game_command))
        self.application.add_handler(CallbackQueryHandler(self.handle_button_press))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Envía un mensaje de bienvenida y comienza un nuevo juego."""
        chat_id = update.effective_chat.id
        self.game_controller[chat_id] = GameController()
        
        await update.message.reply_text("¡Bienvenido al Tatetí! Yo soy O y vos sos X. Para jugar, simplemente haz clic en el botón con el número de la casilla.")
        
        await self.send_board_image(update.effective_chat.id, context)

    async def send_board_image(self, chat_id, context: ContextTypes.DEFAULT_TYPE):
        """Renderiza y envía la imagen del tablero con botones."""
        game = self.game_controller.get(chat_id)
        if not game:
            return
        
        board = game.get_board()
        renderer = BoardRenderer(board)
        img = renderer.render()

        # Guardar la imagen en un buffer de memoria
        from io import BytesIO
        img_buffer = BytesIO()
        img.save(img_buffer, "PNG")
        img_buffer.seek(0)

        # Crear el teclado con botones
        keyboard = []
        if not game.is_finished():
            for i in range(3):
                row = []
                for j in range(3):
                    pos = i * 3 + j
                    if board[pos] == " ":
                        button_text = str(pos)
                        callback_data = str(pos)
                    else:
                        button_text = board[pos]
                        callback_data = "no_op" # No hacer nada si la casilla está ocupada
                    row.append(InlineKeyboardButton(button_text, callback_data=callback_data))
                keyboard.append(row)

        # Siempre añadir el botón de reinicio, sin importar el estado del juego
        keyboard.append([InlineKeyboardButton("Reiniciar juego", callback_data="reset")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        # Enviar la imagen y el teclado
        if game.is_finished():
            winner = game.get_winner()
            if winner == "X":
                message = "¡Ganaste! 🎉"
            elif winner == "O":
                message = "La IA ganó. Mejor suerte la próxima."
            else:
                message = "Empate!"
            
            # Enviar el mensaje final y el teclado con solo el botón de reinicio
            await context.bot.send_photo(chat_id=chat_id, photo=img_buffer, caption=message, reply_markup=reply_markup)
        else:
            # Enviar la imagen y el teclado completo
            await context.bot.send_photo(chat_id=chat_id, photo=img_buffer, caption="Tu turno (X):", reply_markup=reply_markup)

    async def handle_button_press(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Maneja las pulsaciones de los botones del tablero."""
        query = update.callback_query
        await query.answer()
        chat_id = query.message.chat_id
        game = self.game_controller.get(chat_id)
        
        # Lógica para el botón de reinicio
        if query.data == "reset":
            if game:
                game.reset_game()
            else:
                self.game_controller[chat_id] = GameController()
            await self.send_board_image(chat_id, context)
            return
        if not game or game.is_finished():
            return

        # Lógica para el manejo de jugadas    
        move = int(query.data)
        
        if game.player_move(move):
            # Jugada del jugador
            await self.send_board_image(chat_id, context)
            
            # Si el juego no terminó, es el turno de la IA
            if not game.is_finished():
                ai_move = game.ai_move()
                await self.send_board_image(chat_id, context)
        else:
            # Jugada inválida, informar al usuario
            await context.bot.send_message(chat_id=chat_id, text="Casilla ocupada o jugada inválida. Probá otra.")

    async def reset_game_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Reinicia el juego y envía el nuevo tablero."""
        chat_id = update.effective_chat.id
        if chat_id in self.game_controller:
            self.game_controller[chat_id].reset_game()
        else:
            self.game_controller[chat_id] = GameController()
            
        await update.message.reply_text("Juego reiniciado. ¡Buena suerte!")
        await self.send_board_image(chat_id, context)

    def run(self):
        """Inicia el bot."""
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)