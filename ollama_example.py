import requests

def query_ollama(prompt):
    try:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=data)
        return response.json()["response"]

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    result = query_ollama(user_input)
    print("Response:")
    print(result)