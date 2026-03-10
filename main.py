from flask import Flask
import threading
import scheduler
from telegram_fetch import start_telegram_listener

app = Flask(__name__)

@app.route("/")
def home():
    return "Auto Reel Bot Running"


def run_scheduler():
    scheduler.start_scheduler()


def run_telegram():
    start_telegram_listener()


if __name__ == "__main__":

    # scheduler background
    threading.Thread(target=run_scheduler).start()

    # telegram bot background
    threading.Thread(target=run_telegram).start()

    # IMPORTANT FOR RENDER
    app.run(host="0.0.0.0", port=10000)
