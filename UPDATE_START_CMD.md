# 🚀 НОВАЯ КОНФИГУРАЦИЯ для Render

## На Render измените:

### Build Command:
```
pip install -r requirements.txt
```

### Start Command:
```
python main.py
```

⚠️ **ВАЖНО:** Измените Start Command на `python main.py` вместо `python bot.py`!

## Зачем нужен main.py?

Render требует, чтобы Web Service имел открытый порт для health check.
Файл `main.py` запускает:
- Flask сервер на порту (для Render health check)
- Telegram бота в отдельном потоке (для работы)

## Файлы добавлены:
- ✅ `web_server.py` - Flask сервер для health check
- ✅ `main.py` - запускает и Flask и бота
- ✅ `requirements.txt` - добавлен Flask

Отправьте все на GitHub и обновите Start Command на Render!


