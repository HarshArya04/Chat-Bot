import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

import base64 # convert bits to binary

image_path = r"Z:\ChatBot\Medical-Chat-Bot\Data\acne.jpg" # path to image
image_file = open(image_path, "rb")
encoded_image = base64.b64encode(image_file.read()).decode("utf-8")

from groq import Groq

client=Groq()
query = "is there something wrong with my face?"
model="llama-3.2-90b-vision-preview"
messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{encoded_image}",
                },
            },
        ],
    }
]
chat_completion=client.chat.completions.create(
    messages=messages,
    model=model,
)

print(chat_completion.choices[0].message.content)