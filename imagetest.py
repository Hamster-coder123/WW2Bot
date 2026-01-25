from groq import Groq
from dotenv import load_dotenv
import base64
import os
load_dotenv()


def imageinput(imageprompt, userimage):
# Function to encode the image
    def encode_image(image_file):
        # with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = userimage

    # Getting the base64 string
    base64_image = encode_image(image_path)

    client = Groq(api_key=os.getenv("groqkey"))

    chat_completion = client.chat.completions.create(
        
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text":imageprompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )
    
    return(chat_completion.choices[0].message.content)


# userimage = "smiley.jpg"
# imageprompt = "What is this picture?"

# print(imageinput(userimage, userimage))
