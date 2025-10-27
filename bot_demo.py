#!/usr/bin/env python3
"""
Telegram News Bot - Демонстрационная версия
Показывает функционал бота без реального подключения к Telegram
"""

import os
import json
import logging
from datetime import datetime
from typing import Dict, List
import requests
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
        self.news_api_url = 'https://newsapi.org/v2/everything'
        
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
    
    def get_news(self, query: str, language: str = 'ru') -> List[Dict]:
        """Получает новости по запросу из NewsAPI"""
        try:
            if not self.news_api_key or self.news_api_key == 'test_key':
                logger.warning("API ключ для новостей не настроен, возвращаем тестовые новости")
                return self.get_test_news(query)
            
            params = {
                'q': query,
                'language': language,
                'sortBy': 'publishedAt',
                'pageSize': 10,
                'apiKey': self.news_api_key
            }
            
            response = requests.get(self.news_api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            return data.get('articles', [])
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при получении новостей: {e}")
            return self.get_test_news(query)
        except Exception as e:
            logger.error(f"Неожиданная ошибка при получении новостей: {e}")
            return self.get_test_news(query)
    
    def get_test_news(self, query: str) -> List[Dict]:
        """Возвращает тестовые новости"""
        return [
            {
                'title': f'Новости о "{query}" - важные события',
                'description': f'Обзор последних событий в области {query}. Интересные факты и тенденции развития.',
                'url': 'https://example.com/news1',
                'publishedAt': datetime.now().isoformat()
            },
            {
                'title': f'Развитие {query} в 2024 году',
                'description': f'Анализ текущего состояния и перспектив развития {query}. Экспертные мнения и прогнозы.',
                'url': 'https://example.com/news2',
                'publishedAt': datetime.now().isoformat()
            },
            {
                'title': f'Инновации в сфере {query}',
                'description': f'Новые технологии и подходы в области {query}. Практические примеры применения.',
                'url': 'https://example.com/news3',
                'publishedAt': datetime.now().isoformat()
            }
        ]
    
    def filter_news_by_keywords(self, articles: List[Dict], keywords: List[str]) -> List[Dict]:
        """Фильтрует новости по ключевым словам"""
        if not keywords:
            return articles
        
        filtered_articles = []
        for article in articles:
            title = article.get('title', '').lower()
            description = article.get('description', '').lower()
            content = f"{title} {description}"
            
            if any(keyword.lower() in content for keyword in keywords):
                filtered_articles.append(article)
        
        return filtered_articles
    
    def format_news_message(self, articles: List[Dict], topic: str) -> str:
        """Форматирует новости для отправки в Telegram"""
        if not articles:
            return f"📰 По теме '{topic}' новостей не найдено."
        
        message = f"📰 <b>Новости по теме: {topic}</b>\n\n"
        
        for i, article in enumerate(articles[:5], 1):  # Показываем только первые 5 новостей
            title = article.get('title', 'Без заголовка')
            description = article.get('description', '')
            url = article.get('url', '')
            published_at = article.get('publishedAt', '')
            
            # Форматируем дату
            try:
                if published_at:
                    date_obj = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                    formatted_date = date_obj.strftime('%d.%m.%Y %H:%M')
                else:
                    formatted_date = 'Дата неизвестна'
            except:
                formatted_date = 'Дата неизвестна'
            
            message += f"{i}. <b>{title}</b>\n"
            if description:
                message += f"   {description[:200]}{'...' if len(description) > 200 else ''}\n"
            if url:
                message += f"   🔗 <a href='{url}'>Читать далее</a>\n"
            message += f"   📅 {formatted_date}\n\n"
        
        return message
    
    def add_user_topic(self, user_id: int, topic: str, keywords: List[str] = None) -> None:
        """Добавляет тему для пользователя"""
        if user_id not in self.users_data:
            self.users_data[user_id] = {
                'topics': [],
                'keywords': [],
                'daily_digest': True,
                'last_digest': None
            }
        
        if keywords is None:
            keywords = []
        
        self.users_data[user_id]['topics'].append({
            'name': topic,
            'keywords': keywords,
            'added_at': datetime.now().isoformat()
        })
        
        self.save_data()
    
    def remove_user_topic(self, user_id: int, topic: str) -> bool:
        """Удаляет тему у пользователя"""
        if user_id not in self.users_data:
            return False
        
        topics = self.users_data[user_id]['topics']
        self.users_data[user_id]['topics'] = [t for t in topics if t['name'] != topic]
        
        self.save_data()
        return True
    
    def get_user_topics(self, user_id: int) -> List[Dict]:
        """Получает темы пользователя"""
        if user_id not in self.users_data:
            return []
        return self.users_data[user_id].get('topics', [])
    
    def toggle_daily_digest(self, user_id: int) -> bool:
        """Переключает ежедневные дайджесты для пользователя"""
        if user_id not in self.users_data:
            self.users_data[user_id] = {
                'topics': [],
                'keywords': [],
                'daily_digest': True,
                'last_digest': None
            }
        
        self.users_data[user_id]['daily_digest'] = not self.users_data[user_id]['daily_digest']
        self.save_data()
        return self.users_data[user_id]['daily_digest']

def demo_bot():
    """Демонстрация работы бота"""
    print("🚀 Демонстрация Telegram News Bot")
    print("=" * 50)
    
    # Создаем экземпляр бота
    bot = NewsBot()
    
    # Демонстрируем добавление тем
    print("\n📝 Добавляем темы для пользователя:")
    bot.add_user_topic(12345, "искусственный интеллект", ["машинное обучение", "нейросети"])
    bot.add_user_topic(12345, "программирование", ["python", "javascript"])
    bot.add_user_topic(12345, "технологии")
    
    # Показываем темы пользователя
    print("\n📋 Темы пользователя:")
    topics = bot.get_user_topics(12345)
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic['name']}")
        if topic.get('keywords'):
            print(f"   Ключевые слова: {', '.join(topic['keywords'])}")
    
    # Демонстрируем получение новостей
    print("\n📰 Получение новостей:")
    for topic in topics[:2]:  # Берем первые 2 темы
        topic_name = topic['name']
        keywords = topic.get('keywords', [])
        
        print(f"\n🔍 Поиск новостей по теме: '{topic_name}'")
        articles = bot.get_news(topic_name)
        
        if keywords:
            print(f"🔍 Фильтрация по ключевым словам: {', '.join(keywords)}")
            articles = bot.filter_news_by_keywords(articles, keywords)
        
        message = bot.format_news_message(articles, topic_name)
        print(f"\n📱 Сообщение для Telegram:")
        print("-" * 30)
        print(message)
        print("-" * 30)
    
    # Показываем сохраненные данные
    print(f"\n💾 Данные сохранены в файл: {bot.data_file}")
    print("📊 Структура данных:")
    print(json.dumps(bot.users_data, ensure_ascii=False, indent=2))
    
    print("\n✅ Демонстрация завершена!")
    print("\n📝 Для запуска реального бота:")
    print("1. Получите токен у @BotFather в Telegram")
    print("2. Добавьте токен в файл .env")
    print("3. Используйте Python 3.9-3.11 для совместимости")
    print("4. Запустите: python3 bot.py")

def main():
    """Основная функция"""
    print("🤖 Telegram News Bot - Демонстрационная версия")
    print("=" * 60)
    
    # Проверяем конфигурацию
    bot_token = os.getenv('BOT_TOKEN')
    news_api_key = os.getenv('NEWS_API_KEY')
    
    print(f"🔑 BOT_TOKEN: {'✅ Настроен' if bot_token and bot_token != 'your_bot_token_here' else '❌ Не настроен'}")
    print(f"📰 NEWS_API_KEY: {'✅ Настроен' if news_api_key and news_api_key != 'your_news_api_key_here' else '❌ Не настроен'}")
    
    if not bot_token or bot_token == 'your_bot_token_here':
        print("\n⚠️  Реальный бот не может быть запущен без токена!")
        print("🔄 Запускаем демонстрацию функционала...")
        demo_bot()
    else:
        print("\n🚀 Попытка запуска реального бота...")
        print("❌ К сожалению, текущая версия Python (3.14) несовместима с python-telegram-bot")
        print("💡 Рекомендации:")
        print("   - Используйте Python 3.9, 3.10 или 3.11")
        print("   - Или обновите python-telegram-bot до версии, совместимой с Python 3.14")
        demo_bot()

if __name__ == '__main__':
    main()



