from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def add_time(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text("Use: /addtime 20:00")
        return

    new_time = context.args[0]

    with open("data/schedule.txt", "a") as f:
        f.write(new_time + "\n")

    await update.message.reply_text(f"New time {new_time} added")


async def show_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):

    with open("data/schedule.txt", "r") as f:
        schedule = f.read()

    await update.message.reply_text("Current schedule:\n" + schedule)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("addtime", add_time))
app.add_handler(CommandHandler("schedule", show_schedule))

app.run_polling()
