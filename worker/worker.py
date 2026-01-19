import time
import schedule
from datetime import datetime


def sample_task():
    """Sample scheduled task"""
    print(f"[{datetime.now()}] Running scheduled task...")


def main():
    """Main worker loop"""
    print("Worker started. Scheduling tasks...")
    
    # Schedule sample task every hour
    schedule.every().hour.do(sample_task)
    
    # Run immediately once
    sample_task()
    
    # Keep the worker running
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()
