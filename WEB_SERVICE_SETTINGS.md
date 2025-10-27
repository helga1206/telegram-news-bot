# Web Service Settings for Telegram Bot on Render

## ⚙️ Настройки для Web Service:

### Basic Settings:
- **Name:** `telegram-news-bot`
- **Region:** Frankfurt, Germany
- **Branch:** `main`
- **Root Directory:** (пусто)

### Build & Start:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python bot.py`

⚠️ **ВАЖНО:** Измените Start Command на `python bot.py` вместо gunicorn!

### Environment Variables:
Добавьте:
```
BOT_TOKEN=ваш_токен_от_botfather
NEWS_API_KEY=опционально
```

### Advanced Settings:
1. **Health Check:** Отключите (оставить пустым) или используйте простой endpoint
2. **Auto-Deploy:** Включите если нужно автоматическое обновление

### Примечание о Web Service:
Web Service просыпается при получении HTTP запроса.
Для Telegram бота это не требуется - бот сам опрашивает Telegram API.
Это нормально для ботов!

