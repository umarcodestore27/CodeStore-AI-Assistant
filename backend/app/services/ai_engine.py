import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ollama_chat(prompt):
    try:
        # Smart model selection
        if any(x in prompt.lower() for x in ["code", "python", "error"]):
            model = "deepseek-coder:latest"
        else:
            model = "llama3.1:latest"

        res = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        data = res.json()
        return data.get("response", "No response")

    except Exception as e:
        return f"⚠️ Error: {str(e)}"