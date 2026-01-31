from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
from google import genai

client = OpenAI(
    api_key=os.getenv("groqkey"),
    base_url="https://api.groq.com/openai/v1",
)

# userinput = ("")

# while(userinput !="quit"): 
#     print(userinput)
#     userinput = input("What would you like to know?")

#     response = client.responses.create(
#         input=userinput,
#         model="openai/gpt-oss-20b",
#     )
#     print(response.output_text)
#     print(userinput)




def bot(userinput):
    
    response = client.responses.create(
        input=userinput,
        model="openai/gpt-oss-120b",
        
    )
    # for chunk in response:
    #     yield chunk.output_text
    
    return response.output_text

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    # client = genai.Client(api_key=os.getenv("gemkey"))

    # response = client.models.generate_content(
    #     model="gemini-3-pro-preview", contents= userinput
    # )
    # # print(response.text)
    # return response.text




    # import base64
    # from openai import OpenAI

    # client = OpenAI()

    # # Function to encode the image
    # def encode_image(image_path):
    #     with open(image_path, "rb") as image_file:
    #         return base64.b64encode(image_file.read()).decode("utf-8")


    # # Path to your image
    # image_path = "path_to_your_image.jpg"

    # # Getting the Base64 string
    # base64_image = encode_image(image_path)


    # response = client.responses.create(
    #     model="gpt-4.1",
    #     input=[
    #         {
    #             "role": "user",
    #             "content": [
    #                 { "type": "input_text", "text": "what's in this image?" },
    #                 {
    #                     "type": "input_image",
    #                     "image_url": f"data:image/jpeg;base64,{base64_image}",
    #                 },
    #             ],
    #         }
    #     ],
    # )

    # print(response.output_text)














# def generate_stream(prompt: str):
#     stream = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         stream=True,
#     )

    