# 🚀 Деплой на Render - Background Worker

## ✅ Шаг 1: Создайте Background Worker

1. **Откройте Render Dashboard:**
   - https://render.com
   - Нажмите "New" (синяя кнопка вверху)

2. **Выберите "Background Worker"** (НЕ Web Service!)

3. **Настройте:**
   - **Source:** GitHub (подключите ваш репозиторий)
   - **Repository:** `helga1206/telegram-news-bot`
   - **Branch:** `main`
   - **Name:** `telegram-news-bot`
   - **Region:** Frankfurt, Germany (ближайший)
   - **Root Directory:** (оставьте пустым)
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - **Plan:** Free

4. **Нажмите "Create Background Worker"**

## 🔑 Шаг 2: Добавьте переменные окружения

После создания сервиса:

1. Откройте ваш сервис
2. Перейдите в раздел **"Environment"**
3. Добавьте переменные:
   - Key: `BOT_TOKEN`
   - Value: ваш токен от BotFather
   
   - Key: `NEWS_API_KEY` (опционально)
   - Value: ваш ключ NewsAPI

4. Нажмите "Save Changes"

## 📊 Шаг 3: Проверьте деплой

1. Перейдите в **"Logs"**
2. Подождите завершения деплоя (2-3 минуты)
3. Найдите сообщение: **"Бот запущен!"**
4. Если есть ошибки — они будут видны в логах

## ✅ Готово!

Ваш бот работает в облаке Render 24/7!

**Проверка:**
- Откройте Telegram
- Найдите вашего бота
- Отправьте `/start`
- Попробуйте `/weather Москва`

## 🔄 Автоматический деплой

После каждого `git push` на GitHub:
- Render автоматически задеплоит новую версию
- Бот автоматически перезапустится

**Преимущества:**
- ✅ Полностью бесплатно
- ✅ Автоматический деплой
- ✅ Логи в реальном времени
- ✅ Бот работает 24/7

## 📞 Если возникли проблемы:

1. Проверьте логи в Render Dashboard
2. Убедитесь что BOT_TOKEN добавлен
3. Проверьте что Start Command: `python bot.py`
4. Убедитесь что выбран Background Worker, а не Web Service




