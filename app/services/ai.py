import os
import openai
import requests
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DOUBAO_API_URL = os.getenv("DOUBAO_API_URL")
DOUBAO_API_KEY = os.getenv("DOUBAO_API_KEY")

def ask_openai(question: str):
    openai.api_key = OPENAI_API_KEY
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=300
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"OpenAI error: {str(e)}"

def ask_deepseek(question: str):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"messages": [{"role": "user", "content": question}]}
    try:
        resp = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json().get("choices", [{}])[0].get("message", {}).get("content", "No answer from DeepSeek.")
    except Exception as e:
        return f"DeepSeek error: {str(e)}"

def ask_doubot(question: str):
    headers = {
        "Authorization": f"Bearer {DOUBAO_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"messages": [{"role": "user", "content": question}]}
    try:
        resp = requests.post(DOUBAO_API_URL, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        return resp.json().get("choices", [{}])[0].get("message", {}).get("content", "No answer from 豆包.")
    except Exception as e:
        return f"豆包 error: {str(e)}"

def ask_ai(question: str, model: str = "openai"):
    if model == "deepseek":
        return ask_deepseek(question)
    elif model == "doubot":
        return ask_doubot(question)
    else:
        return ask_openai(question)