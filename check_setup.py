#!/usr/bin/env python3
"""
Тестовый скрипт для проверки работы бота
"""

import os
from dotenv import load_dotenv

def check_bot_setup():
    """Проверяет настройку бота"""
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    news_api_key = os.getenv('NEWS_API_KEY')
    
    print("🔍 Проверка настроек бота:")
    print("=" * 40)
    
    if bot_token and bot_token != 'your_bot_token_here' and bot_token != '1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-TEST':
        print("✅ BOT_TOKEN: Настроен")
        print(f"   Токен: {bot_token[:10]}...{bot_token[-10:]}")
    else:
        print("❌ BOT_TOKEN: Не настроен или тестовый")
        print("   Получите токен у @BotFather в Telegram")
    
    if news_api_key and news_api_key != 'your_news_api_key_here' and news_api_key != 'test_key':
        print("✅ NEWS_API_KEY: Настроен")
        print(f"   Ключ: {news_api_key[:10]}...{news_api_key[-10:]}")
    else:
        print("⚠️  NEWS_API_KEY: Не настроен (бот будет показывать тестовые новости)")
    
    print("\n📋 Следующие шаги:")
    if not bot_token or bot_token in ['your_bot_token_here', '1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-TEST']:
        print("1. Получите токен у @BotFather")
        print("2. Отредактируйте файл .env")
        print("3. Запустите: python3.9 bot.py")
    else:
        print("1. Запустите: python3.9 bot.py")
        print("2. Найдите вашего бота в Telegram")
        print("3. Отправьте команду /start")

if __name__ == '__main__':
    check_bot_setup()




