from openai import OpenAI
import os

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACE_API_KEY")
)

def query_huggingface(prompt):
    try:
        completion = client.chat.completions.create(
            model="moonshotai/Kimi-K2-Instruct-0905",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    print("Querying Hugging Face...")
    result = query_huggingface(user_input)
    print("Response:")
    print(result)