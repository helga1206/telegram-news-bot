# Dockerfile для Telegram News Bot
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY bot.py .
COPY env.example .

# Создаем директорию для данных
RUN mkdir -p /app/data

# Запускаем бота
CMD ["python", "bot.py"]



