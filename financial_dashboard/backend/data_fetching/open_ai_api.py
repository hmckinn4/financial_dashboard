import openai

# Use your own API key
openai.api_key = 'your_api_key'

def query_openai(prompt):
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=100)
    return response.choices[0].text

if __name__ == "__main__":
    prompt = "Tell me about the recent performance of Apple stock."
    print(query_openai(prompt))
