from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "توکن اینجا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("➕ ثبت رفرال", callback_data="add")],
        [InlineKeyboardButton("🔍 دیدن رفرال‌ها", callback_data="list")]
    ]

    await update.message.reply_text(
        "👋 سلام!\nبه بات تبادل رفرال خوش اومدی",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
