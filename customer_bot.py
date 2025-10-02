# customer_bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8252741242:AAHzol-99KfuEXXIUscQWj2xyOK0z6izqtk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏮 Welcome to the Dragon Boat Bot!\nType /help to see all commands."
    )

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

async def events(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Next Dragon Boat event: 12 October, Wellington Waterfront.")

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Race Schedule:\n- 9:00 AM Heats\n- 1:00 PM Finals")

async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 Teams of 20 paddlers, 1 drummer, 1 sweep. Safety gear required.")

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Visit our website to register or contact organizers via /contact.")

async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📍 Locations: Wellington Waterfront, Queen's Wharf, more on our website.")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 Email: dragonboat@events.nz\nPhone: +64 4 123 4567")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏆 Dragon Boat Racing promotes fun, fitness, and community spirit.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    handlers = {
        "start": start, "help": help_cmd, "events": events,
        "schedule": schedule, "rules": rules, "register": register,
        "location": location, "contact": contact, "about": about
    }
    for cmd, func in handlers.items():
        app.add_handler(CommandHandler(cmd, func))

    # polling with fast interval
    app.run_polling(poll_interval=0.5)  # checks Telegram every 0.5 sec

if __name__ == "__main__":
    main()