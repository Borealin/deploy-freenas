import os
import time
import schedule
from deploy_freenas import deploy
from config import parse_config, schedule_job
if __name__ == "__main__":
    configs = parse_config(os.path.join(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'config'
            ),
            'config.py'
        ))
    schedule_job(configs, deploy)
    while True:
        schedule.run_pending()
        time.sleep(1)