import psutil
import subprocess
import time

def lag_reduction_strategy():
    try:
        for process in psutil.process_iter(['pid', 'name']):
            if 'RobloxPlayerBeta.exe' in process.info['name']:
                roblox_pid = process.info['pid']
                subprocess.run(["wmic", "process", "where", f"processid={roblox_pid}", "setpriority", "64"])
                time.sleep(60)
                subprocess.run(["wmic", "process", "where", f"processid={roblox_pid}", "setpriority", "32"])
    except Exception as e:
        pass

if __name__ == '__main__':
    lag_reduction_strategy()
