#!/usr/bin/env python3
"""
Главный файл для запуска бота на Render
Запускает Flask сервер для health check и бота в отдельном потоке
"""

import threading
import os
import sys

def run_bot():
    """Запускает Telegram бота"""
    import bot
    bot.main()

def run_web():
    """Запускает Flask сервер"""
    from web_server import app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)

if __name__ == '__main__':
    # Запускаем бота в отдельном потоке (НЕ daemon!)
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.daemon = False  # Не выключать при выходе основного потока
    bot_thread.start()
    
    # Запускаем Flask сервер в текущем потоке
    print("Starting Flask server...")
    run_web()

