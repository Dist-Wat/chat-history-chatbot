import openai

openai.api_key = "Your_API_KEY"


def chat_with_bot(messages):
    chat_log = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return chat_log.choices[0].message


def main():
    print("--- the chatbot ---")

    chat_history = []

    while True:
        user_input = input("user: ")

        chat_history.append({
                'role': 'system',
                'content': user_input
            })

        bot_response = chat_with_bot(chat_history)
        print(f"Tool: {bot_response['content']}\n")

        chat_history.append({
                'role': 'system',
                'content': bot_response['content']
            })


if __name__ == '__main__':
    main()
