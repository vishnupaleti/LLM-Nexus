import os
import csv 
import time
from threading import Lock
MERRICES_DIR = "data/metrics"
MERRICES_FILE = os.path.join(MERRICES_DIR, "metrics.csv")
file_lock = Lock()
os.makedirs(MERRICES_DIR, exist_ok=True)
if not os.path.exists(MERRICES_FILE):
    with open(MERRICES_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["model", "latency", "response_length","timestamp"])
def log_metrics(model: str, latency: float, response_length: int):
    with file_lock:
        with open(MERRICES_FILE,"a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                model,
                round(latency,3),
                response_length,
                time.time()
            ])

        