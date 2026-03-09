from flask import Flask
import threading
import scheduler
import telegram_fetch

app = Flask(__name__)

@app.route("/")
def home():
    return "Auto Reel Bot Running"

def run_scheduler():
    scheduler.start_scheduler()

def run_telegram():
    telegram_fetch.start_telegram_listener()

threading.Thread(target=run_scheduler).start()
threading.Thread(target=run_telegram).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
