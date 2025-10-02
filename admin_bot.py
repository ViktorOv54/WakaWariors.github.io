# admin_bot.py
import os
import random
import logging
import requests
import asyncio
import psutil
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ==============================
# CONFIGURATION
# ==============================
TOKEN = "8398969139:AAFIH9K_otrnrQ-oeDEQouoS1eybnpzUdxE"  # BOT TOKEN HERE
CHAT_ID = "7440753558"                                   # ADMIN CHAT ID
WEBSITE_URL = "https://wakawarriors.netlify.app/"        # WEBSITE URL

# Log file
LOG_FILE = "website_logs.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ==============================
# CORE COMMANDS
# ==============================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Admin Bot online. Use /admin_help to see commands.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get(WEBSITE_URL, timeout=5)
        if r.status_code == 200:
            msg = f"🟢 {WEBSITE_URL} is UP (200 OK)"
        else:
            msg = f"🟡 {WEBSITE_URL} responded with {r.status_code}"
    except:
        msg = f"🔴 {WEBSITE_URL} is DOWN!"
    await update.message.reply_text(msg)

async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = f.readlines()[-10:]
        await update.message.reply_text("📜 Last logs:\n" + "".join(data))
    else:
        await update.message.reply_text("⚠️ No logs yet.")

async def clear_logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if os.path.exists(LOG_FILE):
        open(LOG_FILE, "w").close()
        await update.message.reply_text("🧹 Logs cleared successfully.")
    else:
        await update.message.reply_text("⚠️ No logs found.")

# ==============================
# HARD-CODED SYSTEM FUNCTIONS
# ==============================

async def db_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpu = random.randint(10, 80)
    ram = random.randint(20, 90)
    disk = random.randint(30, 95)
    msg = f"💻 DB/Server Status (simulated):\nCPU: {cpu}% | RAM: {ram}% | Disk: {disk}%"
    await update.message.reply_text(msg)

async def server_load(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    msg = f"⚡ Server Load:\nCPU: {cpu}% | RAM: {ram}% | Disk: {disk}%"
    await update.message.reply_text(msg)

async def security_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🔐 Security Check:\n"
        "✅ SSL Certificate Valid\n"
        "✅ Firewall Active\n"
        "⚠️ Admin Panel Accessible from Public Internet"
    )
    await update.message.reply_text(msg)

async def error_report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "⚠️ Last Errors:\n"
        "[13:22] DB connection timeout\n"
        "[14:01] User login failed (IP blocked)\n"
        "[15:15] API responded 500 error"
    )
    await update.message.reply_text(msg)

async def optimize_tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tips = (
        "⚡ Optimization Tips:\n"
        "1. Enable caching (Redis/CDN)\n"
        "2. Compress static assets\n"
        "3. Use lazy loading for images\n"
        "4. Minimize API calls"
    )
    await update.message.reply_text(tips)

async def daily_summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users = random.randint(100, 500)
    new_reg = random.randint(5, 20)
    uptime = random.randint(1, 365)
    msg = (
        "📊 Daily Summary:\n"
        f"• Active Users: {users}\n"
        f"• New Registrations: {new_reg}\n"
        f"• Server Uptime: {uptime} days"
    )
    await update.message.reply_text(msg)

async def simulate_backup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "💾 Backup started...\n✅ Backup completed successfully!"
    await update.message.reply_text(msg)

async def panic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🔴 PANIC MODE ACTIVATED!\n"
        "🚨 ALL SYSTEMS DOWN 🚨\n"
        "Contact developers immediately!"
    )
    await update.message.reply_text(msg)

async def admin_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "📖 Admin Commands:\n\n"
        "🟢 Website:\n"
        "/status – Check site status\n"
        "/logs – Show last 10 logs\n"
        "/clear_logs – Clear logs\n\n"
        "🗄 System:\n"
        "/db_status – Show DB status\n"
        "/server_load – Show server load\n"
        "/security_check – Run security audit\n"
        "/error_report – Show last errors\n"
        "/optimize_tips – Performance suggestions\n"
        "/daily_summary – Show daily summary\n"
        "/simulate_backup – Run fake backup\n\n"
        "🚨 Emergency:\n"
        "/panic – PANIC MODE 🚨"
    )
    await update.message.reply_text(msg)

# ==============================
# UPTIME MONITOR
# ==============================

CHECK_INTERVAL = 60  # seconds

async def uptime_task(app: Application):
    """Periodic uptime check for WEBSITE_URL"""
    try:
        r = requests.get(WEBSITE_URL, timeout=5)
        if r.status_code == 200:
            msg = f"🟢 {WEBSITE_URL} is UP (200 OK)"
        else:
            msg = f"🟡 {WEBSITE_URL} responded with {r.status_code}"
    except:
        msg = f"🔴 {WEBSITE_URL} is DOWN!"

    # Log
    logging.info(msg)
    
    # Send alert only if down
    if "DOWN" in msg:
        await app.bot.send_message(chat_id=CHAT_ID, text=msg)

# ==============================
# MAIN
# ==============================

def main():
    app = Application.builder().token(TOKEN).build()

    # Core
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("logs", logs))
    app.add_handler(CommandHandler("clear_logs", clear_logs))

    # New
    app.add_handler(CommandHandler("db_status", db_status))
    app.add_handler(CommandHandler("server_load", server_load))
    app.add_handler(CommandHandler("security_check", security_check))
    app.add_handler(CommandHandler("error_report", error_report))
    app.add_handler(CommandHandler("optimize_tips", optimize_tips))
    app.add_handler(CommandHandler("daily_summary", daily_summary))
    app.add_handler(CommandHandler("simulate_backup", simulate_backup))
    app.add_handler(CommandHandler("panic", panic))
    app.add_handler(CommandHandler("admin_help", admin_help))

    # Start uptime monitoring
    app.job_queue.run_repeating(
        lambda ctx: asyncio.create_task(uptime_task(app)),
        interval=CHECK_INTERVAL,
        first=10
    )

    print("🤖 Admin Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()