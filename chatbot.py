from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()
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

# def generate_stream(prompt: str):
#     stream = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         stream=True,
#     )

    