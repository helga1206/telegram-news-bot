# 📦 Готово к деплою на Railway!

Ваш Telegram News & Weather Bot готов к деплою на [Railway](https://railway.com)!

## ✅ Что было подготовлено:

1. ✅ Git репозиторий инициализирован
2. ✅ Все файлы добавлены в коммит
3. ✅ Dockerfile настроен для Railway
4. ✅ Procfile для запуска бота
5. ✅ requirements.txt обновлен
6. ✅ railway.json с конфигурацией
7. ✅ .gitignore настроен

## 🚀 Инструкция по деплою:

### Шаг 1: Создайте репозиторий на GitHub

1. Перейдите на [github.com](https://github.com)
2. Нажмите кнопку **"+" → "New repository"**
3. Название: `telegram-news-bot` (или другое)
4. Сделайте репозиторий **PUBLIC**
5. **НЕ добавляйте** README, .gitignore или лицензию
6. Нажмите **"Create repository"**

### Шаг 2: Отправьте код на GitHub

Скопируйте URL вашего репозитория и выполните:

```bash
cd /Users/olele/ICT/news-telegram-bot

# Добавьте удаленный репозиторий (замените URL на ваш!)
git remote add origin https://github.com/ваш-username/telegram-news-bot.git

# Переименуйте ветку в main (если нужно)
git branch -M main

# Отправьте код на GitHub
git push -u origin main
```

### Шаг 3: Деплой на Railway

1. **Откройте [railway.app](https://railway.app)**
2. Нажмите **"Start a New Project"**
3. Выберите **"Deploy from GitHub repo"**
4. Авторизуйтесь через GitHub
5. Выберите ваш репозиторий `telegram-news-bot`
6. Railway автоматически начнет деплой

### Шаг 4: Настройте переменные окружения

После деплоя в Railway:

1. Откройте ваш проект
2. Перейдите в раздел **"Variables"**
3. Добавьте переменные:

```env
BOT_TOKEN=ваш_токен_от_botfather
NEWS_API_KEY=ваш_ключ_newsapi_опционально
```

### Шаг 5: Проверьте работу

1. Откройте **"Logs"** в Railway
2. Найдите сообщение: **"Бот запущен!"**
3. Проверьте отсутствие ошибок
4. Откройте Telegram и протестируйте бота!

## 📋 Что дальше?

После успешного деплоя:
- ✅ Ваш бот работает 24/7 в облаке
- ✅ Автоматический рестарт при ошибках
- ✅ Логи доступны в реальном времени
- ✅ Бесплатный тариф: 500 часов/месяц

## 🔄 Обновление бота:

После изменений в коде:
```bash
git add .
git commit -m "Обновление бота"
git push
```

Railway автоматически задеплоит новую версию!

## 📞 Поддержка:

Если возникли проблемы:
- Проверьте логи в Railway Dashboard
- Убедитесь что BOT_TOKEN добавлен
- Следуйте инструкциям в DEPLOYMENT.md

**Удачи с деплоем!** 🚀

