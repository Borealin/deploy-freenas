from typing import List, Optional, TypedDict, Literal
import json
import schedule
TimeScaleLiteral = Literal["seconds", "minutes", "hours", "days", "weeks"]

class Config(TypedDict):
    every: int
    time_scale : TimeScaleLiteral
    at: Optional[str]
    
    
Configs = List[Config]

def parse_config(file_path: str) -> Configs:
    with open(file_path, "r") as f:
        return json.load(f)

def schedule_job(configs: Configs, job):
    for config in configs:
        task = schedule.every(config["every"])
        match config["time_scale"]:
            case "seconds":
                task = task.seconds
            case "minutes":
                task = task.minutes
            case "hours":
                task = task.hours
            case "days":
                task = task.days
            case "weeks":
                task = task.weeks
            case _:
                pass
        if "at" in config and config["at"] is not None:
            task = task.at(config["at"])
        def wrapper():
            job()
            time_of_next_run = schedule.next_run()
            print(f"Next run will be {time_of_next_run}")
        task.do(wrapper)
        
if __name__ == "__main__":
    configs = parse_config("config/config.json")
    schedule_job(configs, lambda: print("hello world"))
    while True:
        schedule.run_pending()