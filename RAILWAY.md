# 🚀 Быстрая инструкция по деплою на Railway

## Что нужно сделать:

### 1. GitHub репозиторий
```bash
# Создайте репозиторий на github.com
# Добавьте remote и отправьте код:
git remote add origin https://github.com/ваш-username/telegram-news-bot.git
git branch -M main
git push -u origin main
```

### 2. Деплой на Railway
- Откройте https://railway.app
- Нажмите "Start a New Project"
- Выберите "Deploy from GitHub repo"
- Выберите ваш репозиторий

### 3. Переменные окружения
В Railway → Variables добавьте:
```
BOT_TOKEN=ваш_токен_от_botfather
```

### 4. Готово! 🎉
Бот автоматически запустится в облаке.

Подробная инструкция: смотрите DEPLOYMENT.md




