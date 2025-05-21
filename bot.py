from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

ADMIN_ID = 566825247

participants = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Use /participate to participate at the giveaway!")

async def participate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user.full_name
    participants.add(user)
    await update.message.reply_text(f"{user}, you have been registered!")

async def lista(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to see the list of participants.")
        return
    
    if participants:
        await update.message.reply_text("Participants:\n" + "\n".join(participants))
    else:
        await update.message.reply_text("No one yet.")

async def estrai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("❌ You are not authorized to use this command.")
        return

    if participants:
        vincitore = random.choice(list(participants))
        await update.message.reply_text(f"🎉 The winner is: {vincitore} 🎉")
    else:
        await update.message.reply_text("No participants to be drawn.")

app = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("participate", participate))
app.add_handler(CommandHandler("lista", lista))
app.add_handler(CommandHandler("estrai", estrai))

print("Bot avviato.")
app.run_polling()
