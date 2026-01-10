import streamlit as st
from chatbot import bot
from pdfreader import pdfread 

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
    file_type=["txt", "pdf"],
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
    
    

    with st.chat_message("user"):
        st.write(prompt.text)
    st.session_state['prompthistory'].append(prompt.text)
    
    with st.chat_message("Assistant"):

        if(not prompt["files"]):
            answer = bot(history + prompt.text)
        else:
            if(prompt["files"][0].type == "application/pdf"):
                answer = bot(history + prompt.text + pdfread(prompt["files"][0]))
            else:
                answer = bot(history + prompt.text + str(prompt["files"][0].getvalue()))

        st.write(answer)

    st.session_state['responsehistory'].append(answer)


    





