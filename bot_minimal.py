#!/usr/bin/env python3
"""
Telegram News Bot - Минимальная версия
Бот для сбора новостей по определенным темам
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, List
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class NewsBot:
    """Основной класс для работы с новостным ботом"""
    
    def __init__(self):
        self.data_file = 'news_data.json'
        self.users_data = self.load_data()
        self.news_api_key = os.getenv('NEWS_API_KEY')
        
    def load_data(self) -> Dict:
        """Загружает данные пользователей из JSON файла"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            logger.error(f"Ошибка при загрузке данных: {e}")
            return {}
    
    def save_data(self) -> None:
        """Сохраняет данные пользователей в JSON файл"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.users_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"Ошибка при сохранении данных: {e}")
    
    def get_test_news(self, query: str) -> List[Dict]:
        """Возвращает тестовые новости"""
        return [
            {
                'title': f'Тестовая новость по теме "{query}"',
                'description': 'Это тестовая новость для демонстрации работы бота. В реальной версии здесь будут настоящие новости из NewsAPI.',
                'url': 'https://example.com',
                'publishedAt': datetime.now().isoformat()
            },
            {
                'title': f'Еще одна новость о "{query}"',
                'description': 'Вторая тестовая новость для демонстрации функционала бота.',
                'url': 'https://example.com',
                'publishedAt': datetime.now().isoformat()
            }
        ]
    
    def format_news_message(self, articles: List[Dict], topic: str) -> str:
        """Форматирует новости для отправки в Telegram"""
        if not articles:
            return f"📰 По теме '{topic}' новостей не найдено."
        
        message = f"📰 <b>Новости по теме: {topic}</b>\n\n"
        
        for i, article in enumerate(articles[:3], 1):  # Показываем только первые 3 новости
            title = article.get('title', 'Без заголовка')
            description = article.get('description', '')
            url = article.get('url', '')
            
            message += f"{i}. <b>{title}</b>\n"
            if description:
                message += f"   {description[:150]}{'...' if len(description) > 150 else ''}\n"
            if url:
                message += f"   🔗 <a href='{url}'>Читать далее</a>\n"
            message += "\n"
        
        return message
    
    def add_user_topic(self, user_id: int, topic: str) -> None:
        """Добавляет тему для пользователя"""
        if user_id not in self.users_data:
            self.users_data[user_id] = {'topics': []}
        
        self.users_data[user_id]['topics'].append({
            'name': topic,
            'added_at': datetime.now().isoformat()
        })
        
        self.save_data()
    
    def get_user_topics(self, user_id: int) -> List[Dict]:
        """Получает темы пользователя"""
        if user_id not in self.users_data:
            return []
        return self.users_data[user_id].get('topics', [])

# Создаем экземпляр бота
news_bot = NewsBot()

def start(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /start"""
    username = update.effective_user.username or "пользователь"
    
    welcome_message = f"""
👋 Привет, {username}!

Я бот для сбора и отправки новостей по интересующим вас темам.

<b>Доступные команды:</b>
/start - Начать работу с ботом
/add_topic - Добавить тему для отслеживания
/my_topics - Показать мои темы
/get_news - Получить новости по теме
/help - Показать справку

<b>Как использовать:</b>
1. Добавьте интересующие вас темы командой /add_topic
2. Получайте новости командой /get_news

<b>Пример:</b>
/add_topic программирование
/get_news программирование
"""
    
    update.message.reply_text(welcome_message, parse_mode='HTML')

def add_topic(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /add_topic"""
    user_id = update.effective_user.id
    
    if not context.args:
        update.message.reply_text(
            "Использование: /add_topic <тема>\n"
            "Пример: /add_topic искусственный интеллект"
        )
        return
    
    topic = ' '.join(context.args)
    news_bot.add_user_topic(user_id, topic)
    
    update.message.reply_text(f"✅ Тема '{topic}' добавлена!")

def my_topics(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /my_topics"""
    user_id = update.effective_user.id
    topics = news_bot.get_user_topics(user_id)
    
    if not topics:
        update.message.reply_text("📝 У вас пока нет добавленных тем.")
        return
    
    message = "📝 <b>Ваши темы:</b>\n\n"
    for i, topic_data in enumerate(topics, 1):
        topic_name = topic_data['name']
        added_at = topic_data.get('added_at', '')
        
        message += f"{i}. <b>{topic_name}</b>\n"
        if added_at:
            try:
                date_obj = datetime.fromisoformat(added_at)
                formatted_date = date_obj.strftime('%d.%m.%Y')
                message += f"   📅 Добавлено: {formatted_date}\n"
            except:
                pass
        message += "\n"
    
    update.message.reply_text(message, parse_mode='HTML')

def get_news(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /get_news"""
    if not context.args:
        update.message.reply_text(
            "Использование: /get_news <тема>\n"
            "Пример: /get_news искусственный интеллект"
        )
        return
    
    topic = ' '.join(context.args)
    
    # Получаем тестовые новости
    articles = news_bot.get_test_news(topic)
    message = news_bot.format_news_message(articles, topic)
    
    update.message.reply_text(message, parse_mode='HTML', disable_web_page_preview=True)

def help_command(update: Update, context: CallbackContext) -> None:
    """Обработчик команды /help"""
    help_text = """
📖 <b>Справка по командам:</b>

<b>Основные команды:</b>
/start - Начать работу с ботом
/help - Показать эту справку

<b>Управление темами:</b>
/add_topic <тема> - Добавить тему для отслеживания
/my_topics - Показать все ваши темы

<b>Получение новостей:</b>
/get_news <тема> - Получить новости по конкретной теме

<b>Примеры использования:</b>
/add_topic искусственный интеллект
/get_news программирование

<b>Примечание:</b>
Это демонстрационная версия бота с тестовыми новостями.
Для получения реальных новостей нужен API ключ NewsAPI.
"""
    
    update.message.reply_text(help_text, parse_mode='HTML')

def error_handler(update: Update, context: CallbackContext) -> None:
    """Обработчик ошибок"""
    logger.error(f"Ошибка при обработке обновления: {context.error}")

def main() -> None:
    """Основная функция для запуска бота"""
    # Получаем токен бота из переменных окружения
    bot_token = os.getenv('BOT_TOKEN')
    
    if not bot_token or bot_token == 'your_bot_token_here':
        logger.error("BOT_TOKEN не найден в переменных окружения!")
        print("❌ Ошибка: BOT_TOKEN не настроен!")
        print("📝 Для запуска бота:")
        print("1. Получите токен у @BotFather в Telegram")
        print("2. Добавьте токен в файл .env")
        print("3. Запустите бота снова")
        return
    
    # Создаем updater
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher
    
    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("add_topic", add_topic))
    dispatcher.add_handler(CommandHandler("my_topics", my_topics))
    dispatcher.add_handler(CommandHandler("get_news", get_news))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
    # Добавляем обработчик ошибок
    dispatcher.add_error_handler(error_handler)
    
    logger.info("Бот запущен!")
    print("🚀 Telegram News Bot запущен!")
    print("📱 Найдите вашего бота в Telegram и отправьте /start")
    print("⏹️  Для остановки нажмите Ctrl+C")
    
    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()






