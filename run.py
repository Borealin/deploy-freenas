import time
import schedule
from deploy_freenas import deploy
from config import parse_config, schedule_job
if __name__ == "__main__":
    configs = parse_config("config.json")
    schedule_job(configs, deploy)
    while True:
        schedule.run_pending()
        time.sleep(1)