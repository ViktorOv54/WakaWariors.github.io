# devtools_bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import os

TOKEN = "8405735456:AAHlNp7D45afWjI99UQBiDzBYNy0BiG5fYU"
LOG_FILE = "website_logs.txt"
LOCAL_HTML = "index.html"
WEBSITE_URL = "https://wakawarriors.netlify.app/"

# Simulated stats (replace with real DB/API later)
TOTAL_USERS = 150
REGISTERED_USERS = 120
ONLINE_USERS = 15

# Authorized users for shutdown
AUTHORIZED_USERS = [7440753558]  # Replace with your Telegram ID(s)

# ---------------- Command Handlers ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Visit Website", url=WEBSITE_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👨‍💻 Developer Tools Bot ready!\n"
        "Commands:\n"
        "/status, /logs, /errors, /improve_code, /events_summary\n"
        "/usage_stats, /registrations, /online_users, /shutdown",
        reply_markup=reply_markup
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBSITE_URL, timeout=5) as response:
                if response.status == 200:
                    await update.message.reply_text("✅ Server is up and running!")
                else:
                    await update.message.reply_text(f"⚠️ Server responded with status: {response.status}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = f.read()
        await update.message.reply_text(f"📜 Logs:\n{data[:4000]}")
    else:
        await update.message.reply_text("❌ Log file not found!")

async def errors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    errors_list = []
    try:
        if os.path.exists(LOCAL_HTML):
            with open(LOCAL_HTML, "r", encoding="utf-8") as f:
                html = f.read()
            if "<img" in html and "alt=" not in html:
                errors_list.append("⚠️ Some <img> tags are missing alt attributes")
            if "<h1>" not in html:
                errors_list.append("⚠️ No <h1> title found")
            if "<title>" not in html:
                errors_list.append("⚠️ No <title> tag found")
        else:
            errors_list.append("Local HTML file not found")
    except Exception as e:
        errors_list.append(f"Error parsing HTML: {e}")

    if errors_list:
        await update.message.reply_text("\n".join(errors_list))
    else:
        await update.message.reply_text("✅ No major HTML errors detected!")

async def improve_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    suggestions = [
        "💡 Add alt attributes to <img> tags for accessibility",
        "💡 Use semantic tags like <header>, <footer>, <main>",
        "💡 Minify CSS & JS for faster loading",
        "💡 Avoid inline CSS when possible",
        "💡 Ensure proper heading hierarchy (h1 > h2 > h3...)"
    ]
    await update.message.reply_text("\n".join(suggestions))

async def events_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(WEBSITE_URL, timeout=5) as response:
                text = await response.text()
        soup = BeautifulSoup(text, 'html.parser')
        events = [e.text for e in soup.select('.event-title')]
        if events:
            await update.message.reply_text("📅 Upcoming events:\n" + "\n".join(events))
        else:
            await update.message.reply_text("No events found on the website.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error fetching events: {e}")

# ---------------- New Stats Commands ----------------

async def usage_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    percent_used = (REGISTERED_USERS / TOTAL_USERS) * 100
    await update.message.reply_text(f"📊 Website usage: {percent_used:.1f}% of capacity used")

async def registrations(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"📝 Registered users: {REGISTERED_USERS}/{TOTAL_USERS}")

async def online_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💻 Currently online: {ONLINE_USERS} users")

async def visit_website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Open Website", url=WEBSITE_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌐 Click below to visit the website:", reply_markup=reply_markup)

# ---------------- Shutdown Command ----------------

async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id in AUTHORIZED_USERS:
        await update.message.reply_text("🛑 Developer Tools Bot is shutting down...")
        await context.application.stop()
    else:
        await update.message.reply_text("❌ You do not have permission to shut down the bot.")

# ---------------- Main Setup ----------------

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    handlers = {
        "start": start, "status": status, "logs": logs, "errors": errors,
        "improve_code": improve_code, "events_summary": events_summary,
        "usage_stats": usage_stats, "registrations": registrations,
        "online_users": online_users,
        "visit_website": visit_website, "shutdown": shutdown
    }

    for cmd, func in handlers.items():
        app.add_handler(CommandHandler(cmd, func))

    # Faster polling (0.5s)
    app.run_polling(poll_interval=0.5)

if __name__ == "__main__":
    main()