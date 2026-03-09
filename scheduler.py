import schedule
import time
from main import process_next_clip

def run_scheduler():

    schedule.every().day.at("09:00").do(process_next_clip)
    schedule.every().day.at("12:00").do(process_next_clip)
    schedule.every().day.at("15:00").do(process_next_clip)
    schedule.every().day.at("18:00").do(process_next_clip)

    print("Scheduler started")

    while True:
        schedule.run_pending()
        time.sleep(60)
