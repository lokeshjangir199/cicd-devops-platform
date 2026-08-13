import os
import sys
import json
import urllib.request


def analyze_failure(log_text):
    api_key = os.environ["OPENROUTER_API_KEY"]

    prompt = f"""
You are a DevOps troubleshooting assistant.

Analyze this CI/CD failure log.

Provide:
1. Failure summary
2. Root cause
3. Suggested fix
4. Files or components likely involved

Keep the response concise and practical.

CI/CD LOG:
{log_text}
"""

    payload = {
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 500
    }

    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode())

    return result["choices"][0]["message"]["content"]


if __name__ == "__main__":
    log_file = sys.argv[1]

    with open(log_file, "r", encoding="utf-8") as file:
        logs = file.read()

    print(analyze_failure(logs))
