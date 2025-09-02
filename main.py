from openai import OpenAI


def main():

    model = "gpt-4o-mini"

    client = OpenAI()

    system_prompt = """You are an AI-powered travel guide for the culturally rich city of Paris."""
    conversation = [{"role": "system", "content": system_prompt}]

    userMessages = [
        {"role": "user", "content": 'How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?'},
        {"role": "user", "content": "Where is the Arc de Triomphe?"},
        {"role": "user", "content": "What are the must-see artworks at the Louvre Museum?"}
    ]


    for message in userMessages:
        conversation.append(message)
        
        completion = client.chat.completions.create(
            model=model,
            messages=conversation,
            temperature=0,
            max_completion_tokens=100
        )

        print(completion.choices[0].message.content)
        
        assistant_resp = {"role": "assistant", "content": completion.choices[0].message.content}
        conversation.append(assistant_resp)


if __name__ == '__main__':
    main()