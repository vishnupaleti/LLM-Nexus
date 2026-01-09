import pandas as pd
import os
from datetime import datetime

def choose_models(task: str):
    t = (task or "").strip().lower()
    if t == "coding":
        return ["ChatGPT", "LLaMA"]
    if t == "fast response":
        return ["Gemini", "ChatGPT"]
    if t == "cost saving":
        return ["LLaMA", "Gemini"]
    return ["ChatGPT", "Gemini", "LLaMA"]
def generate_report(prompt: str, responses: dict):

    os.makedirs("data/comparision_reports", exist_ok=True)
    rows = []
    for model, output in responses.items():
        rows.append({
            "Model": model,
            "Prompt": prompt,
            "Response": output,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(rows)
    df.to_csv("data/comparision_reports/reports.csv", index=False)
    
    return "data/comparision_reports/reports.csv"