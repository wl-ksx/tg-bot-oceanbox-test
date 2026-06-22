import asyncio
import json
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppData,
)

# ── Config ──────────────────────────────────────────────────────────────────
BOT_TOKEN = "enter here"        # от @BotFather
WEBAPP_URL = "enter here"  #GitHub Pages URL

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

# ── Bot & Dispatcher ─────────────────────────────────────────────────────────
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ── /start ───────────────────────────────────────────────────────────────────
@dp.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(
            text="🐟 Открыть магазин OceanBox",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    ]])
    await message.answer(
        "👋 Привет! Добро пожаловать в <b>OceanBox</b> — магазин свежей рыбы.\n\n"
        "Нажми кнопку ниже, чтобы открыть каталог и оформить заказ 👇",
        reply_markup=keyboard,
        parse_mode="HTML"
    )


# ── Получение данных из Mini App (tg.sendData) ───────────────────────────────
@dp.message(F.web_app_data)
async def handle_order(message: Message):
    data: WebAppData = message.web_app_data

    try:
        order = json.loads(data.data)
    except json.JSONDecodeError:
        await message.answer("❌ Ошибка при разборе заказа.")
        return

    items = order.get("items", [])
    total = order.get("total", 0)

    if not items:
        await message.answer("🛒 Корзина пустая — добавь товары в магазине.")
        return

    lines = "\n".join(
        f"• {i['name']} × {i['qty']} — {i['price'] * i['qty']} ₽"
        for i in items
    )

    text = (
        "✅ <b>Заказ получен!</b>\n\n"
        f"{lines}\n\n"
        f"💰 <b>Итого: {total:,} ₽</b>\n\n"
        "Мы свяжемся с вами для подтверждения доставки."
    )

    await message.answer(text, parse_mode="HTML")

    log.info("New order from user %s: %s", message.from_user.id, order)


# ── Run ──────────────────────────────────────────────────────────────────────
async def main():
    log.info("Starting OceanBox bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
