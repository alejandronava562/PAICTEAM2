# 1
from openai import OpenAI

# 2
client = OpenAI(
)

# 3
user_prompt = "Give me random fact about sustainability."

system_prompt = """
Generate a random fact either about the impact of how long you touch grass, water consumption, and transportation choosing between biking or driving, carbon footprint as it relates to transporation. Make sure you are educating the user to be more sustainable.
"""

# 4
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": user_prompt},
        {"role": "system", "content": system_prompt}
    ]
)

# system prompt

print(response.choices[0].message.content)