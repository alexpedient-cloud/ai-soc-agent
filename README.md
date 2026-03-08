# AI SOC Agent

An AI-powered Security Operations Center (SOC) automation tool built with Python and LLMs.

## Features

* Automated log analysis using AI
* Structured JSON threat reports
* Automated response actions (block IP, isolate host)
* Extensible architecture for security automation

## Architecture

logs.json → AI SOC Agent → LLM Analysis → JSON Alert → Automated Response

## Technologies

* Python
* OpenAI API
* Security automation concepts
* SOC workflows

## Example Output

```
SOC AI Analysis:

{
 "threat_level": "high",
 "recommended_actions": [
  "block ip 192.168.1.45",
  "isolate host server01"
 ]
}
```

## Author

Alin Timicer
