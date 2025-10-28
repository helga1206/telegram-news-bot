#!/usr/bin/env python3
"""
Скрипт для исправления файла данных бота
"""

import json
import os

def fix_data_file():
    """Исправляет файл данных бота"""
    data_file = 'news_data.json'
    
    if not os.path.exists(data_file):
        print("Файл данных не найден")
        return
    
    # Читаем файл как текст, чтобы увидеть дубликаты
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Исходное содержимое файла:")
    print(content)
    print("\n" + "="*50 + "\n")
    
    # Создаем правильную структуру данных
    fixed_data = {}
    
    # Парсим JSON построчно для обработки дубликатов
    lines = content.strip().split('\n')
    current_key = None
    current_data = None
    
    for line in lines:
        line = line.strip()
        if line.startswith('"') and ':' in line:
            # Это ключ пользователя
            key = line.split(':')[0].strip('"')
            if key in fixed_data:
                print(f"Объединяем данные для пользователя {key}")
                # Объединяем темы
                if 'topics' in fixed_data[key] and 'topics' in current_data:
                    fixed_data[key]['topics'].extend(current_data['topics'])
            else:
                fixed_data[key] = {
                    'topics': [],
                    'keywords': [],
                    'daily_digest': True,
                    'last_digest': None
                }
            current_key = key
        elif line.startswith('"name"'):
            # Это тема
            topic_name = line.split(':')[1].strip('",')
            if current_key and 'topics' in fixed_data[current_key]:
                fixed_data[current_key]['topics'].append({
                    'name': topic_name,
                    'keywords': [],
                    'added_at': '2025-10-23T19:37:00.000000'
                })
    
    # Альтернативный подход - создаем чистый файл
    clean_data = {
        "12345": {
            "topics": [
                {
                    "name": "искусственный интеллект",
                    "keywords": ["машинное обучение", "нейросети"],
                    "added_at": "2025-10-23T00:18:30.937939"
                },
                {
                    "name": "программирование", 
                    "keywords": ["python", "javascript"],
                    "added_at": "2025-10-23T00:18:30.938082"
                },
                {
                    "name": "технологии",
                    "keywords": [],
                    "added_at": "2025-10-23T00:18:30.938168"
                }
            ],
            "keywords": [],
            "daily_digest": True,
            "last_digest": None
        },
        "901323292": {
            "topics": [
                {
                    "name": "искусственный",
                    "keywords": ["интеллект"],
                    "added_at": "2025-10-23T19:36:57.482727"
                },
                {
                    "name": "кулинария",
                    "keywords": ["русская кухня"],
                    "added_at": "2025-10-23T19:37:21.840106"
                }
            ],
            "keywords": [],
            "daily_digest": True,
            "last_digest": None
        }
    }
    
    # Сохраняем исправленный файл
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(clean_data, f, ensure_ascii=False, indent=2)
    
    print("Файл данных исправлен!")
    print("Структура данных:")
    for user_id, user_data in clean_data.items():
        print(f"Пользователь {user_id}: {len(user_data['topics'])} тем")
        for topic in user_data['topics']:
            print(f"  - {topic['name']}")

if __name__ == '__main__':
    fix_data_file()




