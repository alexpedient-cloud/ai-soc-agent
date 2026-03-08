import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_logs(log_data):

    prompt = f"""
You are a cybersecurity SOC analyst.

Analyze the logs and return ONLY JSON in this format:

{{
 "threat_level": "",
 "suspicious_events": [],
 "recommended_actions": []
}}

IMPORTANT RULES:
1. Every action must include the target.
2. Example: "block ip 192.168.1.45"
3. Example: "isolate host server01"
4. Do NOT return actions without targets.

Logs:
{log_data}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content