import os
import hupper
from controllers.telegram_bot import TelegramBot

def worker():
    """Esta función es el punto de entrada principal para el bot."""
    # Obtener el token de BotFather.
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not bot_token:
        print("Error: No se encontró la variable de entorno TELEGRAM_BOT_TOKEN.")
        print("Por favor, configura 'export TELEGRAM_BOT_TOKEN=\"tu_token_aqui\"' en tu terminal.")
        return
        
    print("Iniciando bot...")
    bot = TelegramBot(bot_token)
    bot.run()

def main():
    """
    Función principal que inicia el reloader si estamos en modo de desarrollo,
    o el bot directamente si no lo estamos.
    """
    if __name__ == '__main__':
        reloader = hupper.start_reloader('main.worker')
    else:
        worker()

if __name__ == "__main__":
    main()