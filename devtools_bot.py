from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
import os

# 🔑 Replace with your Developer Tools Bot token
TOKEN = "8405735456:AAHlNp7D45afWjI99UQBiDzBYNy0BiG5fYU"

# Path to your log file (change if needed)
LOG_FILE = "website_logs.txt"

# Path to your HTML file (if local)
LOCAL_HTML = "index.html"

# Greeting
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👨‍💻 Developer Tools Bot ready!\n"
        "Use /status, /logs, /errors, /improve_code, /events_summary"
    )

# Check server status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://yourwebsite.com"  # replace with your live site
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            await update.message.reply_text("✅ Server is up and running!")
        else:
            await update.message.reply_text(f"⚠️ Server responded with status: {response.status_code}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# Fetch logs
async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = f.read()
        await update.message.reply_text(f"📜 Logs:\n{data[:4000]}")  # max 4000 chars for Telegram
    else:
        await update.message.reply_text("❌ Log file not found!")

# Detect simple HTML errors
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

# Suggest basic improvements
async def improve_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    suggestions = [
        "💡 Add alt attributes to <img> tags for accessibility",
        "💡 Use semantic tags like <header>, <footer>, <main>",
        "💡 Minify CSS & JS for faster loading",
        "💡 Avoid inline CSS when possible",
        "💡 Ensure proper heading hierarchy (h1 > h2 > h3...)"
    ]
    await update.message.reply_text("\n".join(suggestions))

# Fetch upcoming events
async def events_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://yourwebsite.com"  # replace with your live site
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        events = [e.text for e in soup.select('.event-title')]  # change selector as needed
        if events:
            await update.message.reply_text("📅 Upcoming events:\n" + "\n".join(events))
        else:
            await update.message.reply_text("No events found on the website.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error fetching events: {e}")

# Main setup
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("logs", logs))
    app.add_handler(CommandHandler("errors", errors))
    app.add_handler(CommandHandler("improve_code", improve_code))
    app.add_handler(CommandHandler("events_summary", events_summary))

    app.run_polling()

if __name__ == "__main__":
    main()