import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

WEB_APP_URL = "https://adsrbx.gt.tc/az/"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Başla",
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ]

    await update.message.reply_text(
        "👋 Salam!\n\nBaşlamaq üçün aşağıdakı düyməyə bas 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot işləyir...")
    app.run_polling()


if __name__ == "__main__":
    main()
