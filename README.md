# OceanBox — Telegram Mini App

## Структура файлов
```
index.html   — Mini App (кидаешь на GitHub Pages)
bot.py       — Telegram бот на aiogram 3
```

---

## Шаг 1 — Создать бота

1. Открой @BotFather в Telegram
2. `/newbot` → придумай имя (например `OceanBox Store`) и username (`oceanbox_store_bot`)
3. Скопируй токен вида `7xxxxxxx:AAF...`
4. Вставь в `bot.py` строку `BOT_TOKEN = "..."`

---

## Шаг 2 — Задеплоить Mini App на GitHub Pages

1. Создай новый репозиторий на GitHub (например `oceanbox`)
2. Загрузи `index.html` в корень репозитория
3. Settings → Pages → Source: **Deploy from branch** → `main` / `root`
4. Подожди ~1 минуту, твой URL будет:
   `https://YOUR_USERNAME.github.io/oceanbox/`
5. Вставь этот URL в `bot.py` строку `WEBAPP_URL = "..."`

---

## Шаг 3 — Привязать Mini App к боту (через BotFather)

```
/newapp
→ выбери своего бота
→ Title: OceanBox
→ Description: Магазин свежей рыбы
→ Photo: загрузи любую картинку рыбы
→ Web App URL: https://YOUR_USERNAME.github.io/oceanbox/
```

Теперь приложение доступно по ссылке вида:
`https://t.me/YOUR_BOT_USERNAME/oceanbox`

---

## Шаг 4 — Запустить бота

```bash
pip install aiogram
python bot.py
```

Для продакшна используй systemd, supervisor или запускай в screen/tmux.

---

## Как это работает

1. Пользователь пишет `/start` боту
2. Бот отвечает кнопкой, открывающей Mini App
3. Пользователь добавляет товары, нажимает «Оформить заказ»
4. Mini App вызывает `tg.sendData(JSON)` — данные уходят боту
5. Бот получает заказ через хендлер `F.web_app_data` и отвечает подтверждением

---

## Для портфолио

Прямая ссылка на Mini App без бота:
`https://t.me/YOUR_BOT_USERNAME/oceanbox`

Можно показать клиенту — откроется прямо в Telegram.
