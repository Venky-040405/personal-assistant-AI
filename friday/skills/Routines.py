import subprocess as sp
import pathlib as pl
from friday.setting import CODING_MODE
import psutil

def Daily_routine():

    cfg = CODING_MODE

    opening = []
    closing = []

    for key, value in cfg.items():

        if not pl.Path(cfg["project"]).is_dir():
            return "Project directory not found."

    steps = [
        ("vscode",(cfg["vscode"],cfg["project"])),
        ("brave",(cfg["browser"],*cfg["urls"])),
    ]        

    for labels, value in steps:
        try:
            sp.Popen(value)
            opening.append(labels)
        except Exception as e:
            closing.append(labels)

    reply = "Coding mode is on."
    if opening:
        reply += " Opened " + " and ".join(opening) + "."
    if closing:
        reply += " I couldn't open " + " and ".join(closing) + "."
    return reply        


def battery_status():
    battery = psutil.sensors_battery()
    if battery:
        percent = battery.percent
        plugged = battery.power_plugged
        status = "plugged in" if plugged else "not plugged in"
        return f"Battery is at {percent}% and is currently {status}."
    else:
        return "Battery information is not available."    

def cpu():
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU usage is at {cpu_percent}%."        

def memory():    
    memory = psutil.virtual_memory()
    percent = memory.percent
    return f"Memory usage is at {percent}%."