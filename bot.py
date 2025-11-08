from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7828218009:AAEbNy4fpzdyGW44lJ3VKVWTu1moBwXXpyA"  # 🔑 Mets ton token ici

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salut ! Je suis un bot Telegram Dockerisé.\nEnvoie-moi un message pour tester.")

# Commande /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 Commandes disponibles :\n/start - Démarrer\n/help - Aide\n\nOu écris-moi simplement un message !")

# Réponse automatique aux messages texte
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "bonjour" in text:
        response = "Salut à toi 👋"
    elif "comment" in text and "ça va" in text:
        response = "Je vais super bien 🤖 et toi ?"
    else:
        response = f"Tu as dit : {update.message.text}"

    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot démarré avec succès (mode polling).")
    app.run_polling()

if __name__ == "__main__":
    main()
