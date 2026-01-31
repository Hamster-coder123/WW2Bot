import streamlit as st
from chatbot import bot
from pdfreader import pdfread 
from rag import retrieval
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
load_dotenv()
from imagetest import imageinput
tavily_client = TavilyClient(api_key=os.getenv("tavkey"))


if 'prompthistory' not in st.session_state:
    st.session_state['prompthistory'] = []

if 'responsehistory' not in st.session_state:
    st.session_state['responsehistory'] = []

@st.cache_data
def quest(prompt):
    return bot(prompt)




st.title("Welcome to HamadanGPT", text_alignment= "center")

prompt = st.chat_input(
    "What would you like to know?",
    accept_file=True,
    file_type=["txt", "pdf", "jpg", "png", "jpeg"],
)
# if prompt and prompt.text:
# if prompt and prompt["files"]:
#     st.write(prompt["files"][0].getvalue())

history = ""

for i in range(len(st.session_state['prompthistory'])):
    with st.chat_message("user"):
        st.write(st.session_state['prompthistory'][i])
    with st.chat_message("Assistant"):
        st.write(st.session_state['responsehistory'][i])  
    history += f"User said:{st.session_state['prompthistory'][i]} and Assistant answered with {st.session_state['responsehistory'][i]}"    




if prompt and prompt.text:
    context = retrieval(prompt.text, 2)
    

    with st.chat_message("user"):
        st.write(prompt.text)
        response = tavily_client.search(prompt.text)
    st.session_state['prompthistory'].append(prompt.text)
    
    with st.chat_message("Assistant"):
        # prompt.text += f"This is the context, use only this information to formulate your answer. {context} cite the relevant parts from the metadata as well. {response} This is the data from a recent internet search."
        prompt.text += f"{response} This is the results of a internet search, Create a coherent ouput using these results. If any relevant piece of information is useful to the users prompt,Cite it, and make sure to use it in creating the output"
        

        if(not prompt["files"]):
            answer = bot(history + prompt.text)
        else:
            if(prompt["files"][-1].type == "application/pdf"):
                answer = bot(history + prompt.text + "This is the context provided from a pdf document, use it to formulate your answer:" + pdfread(prompt["files"][0]))
                
            elif(prompt["files"][-1].type.startswith("image/")):
                answer = imageinput(history + prompt.text, prompt["files"][-1])

            else:
                answer = bot(history + prompt.text + str(prompt["files"][-1].getvalue()))

        st.write(answer)
        

    st.session_state['responsehistory'].append(answer)


    





# """pdfread(prompt["files"][0])

# Benito Mussolini’s path to power was a combination of political skill, opportunism and the chaos that gripped post‑war Italy. According to the source material:

# * In 1919 he launched the Fasci di Combattimento, a local‑based nationalist movement that attracted young war veterans and the anti‑socialist middle classes【aea42521-4c8d-460c-8268-ead9885faa64】【80e5bdb8-6ecb-428a-9aeb-68d5dc755f85】.
# * By 1921 the Fascist Party had entered Parliament, winning 35 seats and giving Mussolini a foothold in national politics【aea42521-4c8d-460c-8268-ead9885faa64】【80e5bdb8-6ecb-428a-9aeb-68d5dc755f85】.
# * The political crisis that escalated in 1922 created an opening: King Victor Emmanuel III was forced to invite Mussolini to form a government. In doing so, the monarch handed the reins of executive power to him, effectively making Mussolini the head of a new regime that would soon become a one‑party dictatorship【aea42521-4c8d-460c-8268-ead9885faa64】【80e5bdb8-6ecb-428a-9aeb-68d5dc755f85】.

# Thus, Mussolini’s rise was achieved by first building a popular nationalist movement, then leveraging electoral success to gain a seat in Parliament, and finally exploiting a national crisis to be invited by the king to take over government control.

# """