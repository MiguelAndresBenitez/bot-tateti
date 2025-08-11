# 🤖 Bot de Tatetí para Telegram

Un bot de Telegram que permite jugar al Tatetí contra una IA usando el algoritmo Minimax, con un tablero visual generado como imagen y botones interactivos.

---

## 🚀 Instalación en local

### 1. Clonar repositorio
```bash
git clone https://github.com/usuario/tateti_bot.git
cd tateti_bot

### 2. Crear entorno virtual e instalar dependencias

python3 -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
pip install -r requirements.txt

### 3. Configurar el token del bot

Crea un archivo .env en la raíz del proyecto con:

BOT_TOKEN=TU_TOKEN_AQUI

    Obtén el token creando un bot en Telegram con @BotFather.

### 4. Ejecutar

python main.py

## 📂 Estructura del proyecto

tateti_bot/
├── main.py                  # Punto de entrada del bot
├── controllers/             # Manejo de comandos y flujo del bot
├── models/                  # Clases del juego (TatetiGame)
├── ai/                      # IA Minimax
├── utils/                   # Funciones auxiliares
├── assets/                  # Recursos como imágenes
├── requirements.txt         # Dependencias del proyecto
└── .env                     # Variables de entorno

## ✨ Funcionalidades

    🎮 Juego de Tatetí contra una IA Minimax.

    🖼 Tablero visual generado con PIL.

    📱 Botones interactivos de Telegram.

    🔄 Autoreload con hupper para desarrollo.