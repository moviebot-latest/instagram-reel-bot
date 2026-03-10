import schedule
import time

def job():
    print("Processing reel...")

def start_scheduler():

    schedule.every().day.at("09:00").do(job)
    schedule.every().day.at("12:00").do(job)
    schedule.every().day.at("15:00").do(job)
    schedule.every().day.at("18:00").do(job)

    print("Scheduler running...")

    while True:
        schedule.run_pending()
        time.sleep(30)
