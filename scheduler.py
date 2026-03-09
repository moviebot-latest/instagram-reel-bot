import schedule
import time
from process import process_reel

def start_scheduler():

    schedule.every().day.at("10:00").do(process_reel)
    schedule.every().day.at("13:00").do(process_reel)
    schedule.every().day.at("17:00").do(process_reel)
    schedule.every().day.at("21:00").do(process_reel)

    while True:
        schedule.run_pending()
        time.sleep(20)
