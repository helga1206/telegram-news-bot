# ⚙️ ВАЖНО: Измените Start Command на Render!

## Шаги:

1. **Откройте Render Dashboard:**
   - https://render.com
   - Откройте ваш сервис

2. **Зайдите в Settings:**
   - Settings → "Build & Deploy"

3. **Найдите "Start Command":**
   - Сейчас там: `python bot.py`
   - Измените на: `python main.py`
   - Сохраните (Save Changes)

4. **Или используйте GUI:**
   - Settings → Environment
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python main.py`

5. **Запустите Manual Deploy:**
   - Manual Deploy → "Deploy latest commit"
   - Подождите 2-3 минуты

6. **Проверьте логи:**
   - Должно быть:
   - ✅ "Running on http://0.0.0.0:5000"
   - ✅ "Бот запущен!"
   - ✅ Нет ошибок про порт!

## ✅ После этого:

Render упакует:
- Flask сервер (для health check)
- Telegram бота (в отдельном потоке)

И все будет работать! 🎉

