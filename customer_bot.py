# customer_bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# 🔑 Replace with your Customer Bot token
TOKEN = "8252741242:AAHzol-99KfuEXXIUscQWj2xyOK0z6izqtk"

# Greeting and start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏮 Welcome to the Dragon Boat Bot!\n"
        "Type /help to see all commands."
    )

# Help command
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/events - Upcoming events\n"
        "/schedule - Race schedule\n"
        "/rules - Racing rules\n"
        "/register - Registration info\n"
        "/location - Event locations\n"
        "/contact - Contact organizers\n"
        "/about - About Dragon Boat"
    )

# Events
async def events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Next Dragon Boat event: 12 October, Wellington Waterfront.")

# Schedule
async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Race Schedule:\n- 9:00 AM Heats\n- 1:00 PM Finals")

# Rules
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 Rules: Teams of 20 paddlers, 1 drummer, 1 sweep. Safety gear required.")

# Registration
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Registration Info:\n"
        "Visit our website to register or contact the organizers directly via /contact."
    )

# Location
async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 Event Locations:\n"
        "Wellington Waterfront, Queen's Wharf, and additional locations on our website."
    )

# Contact
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Contact Organizers:\n"
        "Email: dragonboat@events.nz\nPhone: +64 4 123 4567"
    )

# About
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 About Dragon Boat:\n"
        "Dragon Boat Racing is a team paddling sport promoting fun, fitness, and community spirit."
    )

# Main setup
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("events", events))
    app.add_handler(CommandHandler("schedule", schedule))
    app.add_handler(CommandHandler("rules", rules))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("location", location))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("about", about))

    app.run_polling()

if __name__ == "__main__":
    main()