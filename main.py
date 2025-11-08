import json
from openai import OpenAI

client = OpenAI(
)

system_prompt = """
You are a sustainability expert. Help the user live more sustainable by suggesting changes they can make in their lifestyle to be more sustaianable. Give supporting facts from past studies and data. 
"""

def talk_to_chatgpt(system_prompt):
    """
    Allows the user to have a conversation with the ChatGPT API.
    ChatGPT will remember what the user says to it as long as this conversation is active.
    When the function terminates, ChatGPT will forget everything the user said.
    The user can end this conversation by typing and entering "STOP".

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.

    Returns:
    - (list(dict)): The chat history.
    """

    chat_history = [
        {"role": "system", "content": system_prompt},
    ]

    while True:
        user_prompt = input("What are your current lifestyle habits? \n(Type in \"FINISH\" to end this conversation) ")
        if user_prompt == "FINISH":
            return chat_history
        
        chat_history.append(
            {"role": "user", "content": user_prompt},
        )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages = chat_history
        )

        assistant_response = response.choices[0].message.content
        print(assistant_response)
        print()
#hello david I am mamammamamamamjmdjahkudha
        chat_history.append(
            {"role": "assistant", "content": assistant_response}
        )

talk_to_chatgpt(system_prompt)