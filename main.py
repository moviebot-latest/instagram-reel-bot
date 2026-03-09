from flask import Flask
import threading
import scheduler
import telegram_fetch

app = Flask(__name__)

@app.route("/")
def home():
    return "Instagram Auto Reel Bot Running 🚀"


def run_scheduler():
    print("Scheduler starting...")
    scheduler.start_scheduler()


def run_telegram():
    print("Telegram bot starting...")
    telegram_fetch.start_telegram_listener()


# start background services
threading.Thread(target=run_scheduler).start()
threading.Thread(target=run_telegram).start()


if __name__ == "__main__":
    print("Server starting...")
    app.run(host="0.0.0.0", port=10000)
