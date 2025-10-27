# 🆓 Бесплатный деплой на Render.com

## Почему Render?

- ✅ Полностью бесплатно
- ✅ Работает как базовая версия Railway
- ✅ Легко настроить
- ✅ Telegram-боты работают отлично

## 📤 Шаг 1: Отправьте код на GitHub

Выполните в терминале:

```bash
cd /Users/olele/ICT/news-telegram-bot
git remote set-url origin https://github.com/helga1206/telegram-news-bot.git
git branch -M main
git push -u origin main
```

**При запросе пароля:** Используйте Personal Access Token от GitHub

## 🚀 Шаг 2: Деплой на Render

1. **Зарегистрируйтесь:**
   - Откройте https://render.com
   - Нажмите "Get Started for Free"
   - Авторизуйтесь через GitHub

2. **Создайте Web Service:**
   - Нажмите "New" → "Web Service"
   - Выберите ваш репозиторий `helga1206/telegram-news-bot`
   
3. **Настройте:**
   - Name: `telegram-news-bot`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python bot.py`

4. **Добавьте переменные окружения:**
   - BOT_TOKEN=ваш_токен_от_botfather
   - NEWS_API_KEY=опционально

5. **Нажмите "Create Web Service"**

## ✅ Готово!

Render автоматически задеплоит бота!

**Преимущества Render:**
- ✅ Бесплатный план без ограничений
- ✅ Автоматический деплой из GitHub
- ✅ Логи в реальном времени
- ✅ HTTPS из коробки

Подробная инструкция: https://render.com/docs

