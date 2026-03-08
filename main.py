import json
from agent import analyze_logs
from tools import block_ip, isolate_host

with open("logs.json") as f:
    logs = json.load(f)

analysis = analyze_logs(logs)

print("\nSOC AI Analysis:\n")
print(analysis)

result = json.loads(analysis)

for action in result["recommended_actions"]:

    action = action.lower()

    if "block ip" in action:
        ip = action.split()[-1]
        block_ip(ip)

    elif "isolate host" in action:
        host = action.split()[-1]
        isolate_host(host)