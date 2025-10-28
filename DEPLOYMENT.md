# 🚀 Деплой на Railway

## Инструкция по деплою Telegram News & Weather Bot на Railway

### Шаг 1: Подготовка GitHub репозитория

1. **Создайте новый репозиторий на GitHub:**
   - Перейдите на [github.com](https://github.com)
   - Нажмите "New repository"
   - Назовите репозиторий (например: `telegram-news-bot`)
   - Сделайте репозиторий **PUBLIC** (это важно для Railway)

2. **Загрузите код:**
   ```bash
   # В папке проекта
   cd /Users/olele/ICT/news-telegram-bot
   
   # Инициализируйте git (если еще не сделано)
   git init
   
   # Добавьте все файлы
   git add .
   
   # Сделайте первый коммит
   git commit -m "Initial commit: Telegram News & Weather Bot"
   
   # Добавьте remote репозиторий
   git remote add origin https://github.com/ваш-username/telegram-news-bot.git
   
   # Отправьте код на GitHub
   git push -u origin main
   ```

### Шаг 2: Деплой на Railway

1. **Перейдите на Railway:**
   - Откройте [railway.app](https://railway.app)
   - Нажмите "Login with GitHub"
   - Авторизуйтесь через GitHub

2. **Создайте новый проект:**
   - Нажмите "New Project"
   - Выберите "Deploy from GitHub repo"
   - Выберите репозиторий `telegram-news-bot`
   - Railway автоматически обнаружит Dockerfile

3. **Настройте переменные окружения:**
   - После деплоя откройте проект
   - Перейдите в "Variables"
   - Добавьте переменные:

   ```env
   BOT_TOKEN=your_bot_token_from_botfather
   NEWS_API_KEY=your_newsapi_key_optional
   ```

4. **Деплой:**
   - Railway автоматически начнет деплой
   - Дождитесь завершения сборки
   - Проверьте логи на наличие ошибок

### Шаг 3: Проверка работы

1. **Посмотрите логи:**
   - В Railway Dashboard откройте "Logs"
   - Найдите сообщение "Бот запущен!"
   - Проверьте отсутствие ошибок

2. **Проверьте бота:**
   - Откройте Telegram
   - Найдите вашего бота
   - Отправьте `/start`
   - Попробуйте `/weather Москва`

### Важные моменты:

- ✅ Railway автоматически перезапустит бота при ошибках
- ✅ Логи доступны в реальном времени
- ✅ Переменные окружения хранятся безопасно
- ✅ Бот работает 24/7 без перерывов
- ✅ Бесплатный тариф включает 500 часов в месяц

### Обновление бота:

После каждого обновления в GitHub:
```bash
git add .
git commit -m "Обновление бота"
git push
```

Railway автоматически задеплоит новую версию!

### Структура файлов для деплоя:

```
news-telegram-bot/
├── bot.py              # Основной код бота
├── requirements.txt    # Зависимости
├── Dockerfile         # Конфигурация Docker
├── Procfile           # Конфигурация процесса
├── railway.json       # Конфигурация Railway
├── runtime.txt        # Версия Python
├── .gitignore         # Исключения для Git
├── README.md          # Документация
└── env.example        # Пример конфигурации
```

### Поддержка:

Если возникли проблемы:
1. Проверьте логи в Railway Dashboard
2. Убедитесь, что BOT_TOKEN добавлен
3. Проверьте, что код отправлен на GitHub
4. Посмотрите статус деплоя в Railway

**Готово! Ваш бот работает в облаке!** 🎉


