import pandas as pd
import os
from datetime import datetime

def generate_report(prompt: str, responses: dict):
    os.makedirs("reports", exist_ok=True)
    rows = []
    for model, output in responses.items():
        rows.append({
            "Model": model,
            "Prompt": prompt,
            "Response": output,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    df = pd.DataFrame(rows)
    df.to_csv("reports/llm_responses_report.csv", index=False)
    return "reports/llm_responses_report.csv"