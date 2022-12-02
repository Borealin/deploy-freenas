import os
import time
import schedule
import traceback
from deploy_freenas import deploy
from config import parse_config, schedule_job
def safe_deploy():
    try:
        deploy()
    except:
        traceback.print_exc()

if __name__ == "__main__":
    print("start running")
    print("reading configs")
    configs = parse_config(os.path.join(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'config'
            ),
            'config.json'
        ))
    print("configs:")
    print(configs)
    print("scheduling configs")
    schedule_job(configs, safe_deploy)
    while True:
        schedule.run_pending()
        time.sleep(1)