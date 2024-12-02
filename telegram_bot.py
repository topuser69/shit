from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load words from file
with open("english.txt", "r") as file:
    words = file.read().splitlines()

# Command handler for /generate
async def generate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_words = random.sample(words, 12)  # Select 12 random words
    await update.message.reply_text(" ".join(random_words))

# Main function to set up the bot
def main():
    # Initialize the bot with your token
    application = Application.builder().token('7805200067:AAGvmwPMZ-tKpn-RTVKdW-B0fsTJokFPZug').build()

    # Add command handler
    application.add_handler(CommandHandler("generate", generate))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
