#!/usr/bin/env python3
"""
Главный файл для запуска бота на Render
Упрощенная версия для worker service
"""

import os
import sys

def run_bot():
    """Запускает Telegram бота"""
    print("Starting Telegram News Bot...")
    import bot
    bot.main()

if __name__ == '__main__':
    print("Initializing bot...")
    run_bot()

