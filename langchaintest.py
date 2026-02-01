from langchain.tools import tool
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
tavily_client = TavilyClient(api_key=os.getenv("tavkey"))
from rag import retrieval

llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.2,
    api_key=os.getenv("openaikey")
    # stream_usage=True,
    # temperature=None,
    # max_tokens=None,
    # timeout=None,
    # reasoning_effort="low",
    # max_retries=2,
    # api_key="...",  # If you prefer to pass api key in directly
    # base_url="...",
    # organization="...",
    # other params...
)
# # model = init_chat_model(
# #     "gpt-4o-mini",
# #     temperature=0,
# #     api_key=os.getenv("openaikey")
# # )


# # Define tools
# @tool
# def multiply(a: int, b: int) -> int:
#     """Multiply `a` and `b`.

#     Args:
#         a: First int
#         b: Second int
#     """
#     return "Multiply function"


# @tool
# def add(a: int, b: int) -> int:
#     """Adds `a` and `b`.

#     Args:
#         a: First int
#         b: Second int
#     """
#     return "Add function"


# @tool
# def divide(a: int, b: int) -> float:
#     """Divide `a` and `b`.

#     Args:
#         a: First int
#         b: Second int
#     """
#     return a / b


# Augment the LLM with tools
# tools = [add, multiply, divide]
# tools_by_name = {tool.name: tool for tool in tools}
# model_with_tools = llm.bind_tools(tools)

# print(model_with_tools.invoke("What can you do"))


from langchain.agents import create_agent


@tool
def check_weather(location: str) -> str:
    '''Return the weather forecast for the specified location.'''
    return f"It's always sunny in {location}"

@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return "Multiply function"

@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return "Add function"

@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b
@tool
def netsearch(prompt: str) -> str:
    """Can search up any prompt on the internet

    Args:
        a: Search Prompt
    """
    response = tavily_client.search(prompt)
    return response

@tool
def ww2(prompt: str) -> str:
    """Can search up any prompt relating to the second world war or around the same timeframe

    Args:
        a: Search Prompt
    """
    response = retrieval(prompt, 2)
    return response




graph = create_agent(
    model=llm,
    tools=[check_weather, multiply, add, divide, netsearch, ww2],
    system_prompt="Your only job is to understand the question, then to answer it as best as possible, do not ask any follow up questions.",
)
# inputs = {"messages": [{"role": "user", "content": "How many total epstein files have been released to the public"}]}

# output = ""
# for chunk in graph.stream(inputs, stream_mode="updates"):


#     for step, data in chunk.items():
#             output = data['messages'][-1].content_blocks

# print(output[0]["text"])

def chatagent(prompt) -> str:
    inputs = {"messages": [{"role": "user", "content": prompt}]}
    output = ""
    for chunk in graph.stream(inputs, stream_mode="updates"):


        for step, data in chunk.items():
                output = data['messages'][-1].content_blocks
                print(step)
                print(output)

    return output[0]["text"]


print(chatagent("How many US troops were in britain in november 1942 in ww2"))

