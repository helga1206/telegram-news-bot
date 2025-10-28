#!/usr/bin/env python3
"""
Главный файл для запуска бота на Render
Запускает Flask сервер для health check и бота в отдельном потоке
"""

import threading
import os
from web_server import app
from bot import main as bot_main

def run_bot():
    """Запускает Telegram бота"""
    bot_main()

if __name__ == '__main__':
    # Запускаем бота в отдельном потоке
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Запускаем Flask сервер для Render health check
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

