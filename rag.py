from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("openaikey"))
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import chromadb
chroma_client = chromadb.Client()
import uuid
from chromadb.utils import embedding_functions
from pdfreader import pdfread




openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.getenv("openaikey"),
                model_name="text-embedding-3-large"
            )
client = chromadb.PersistentClient(path='db')
collection = client.get_or_create_collection(name="vectordb", embedding_function=openai_ef)

# collection = chroma_client.create_collection(name="my_collection")
# collection = client.get_collection(name="langchain", embedding_function=openai)

# collection.add(
#     ids=["id1", "id2"],
#     documents=[
#         "This is a document about pineapple",
#         "This is a document about oranges"
#     ]
# )


def addtodb(text):
    collection.add(ids = [f"{uuid.uuid4()}"],documents = [text])

    





def embedding_similarity_and_distance(
    emb1: list | np.ndarray,
    emb2: list | np.ndarray
) -> dict:
    """
    Compute cosine similarity and cosine distance between two embedding vectors.

    Args:
        emb1: First embedding vector (list or np.ndarray)
        emb2: Second embedding vector (list or np.ndarray)

    Returns:
        dict with:
            - cosine_similarity
            - cosine_distance (1 - similarity)
    """

    v1 = np.array(emb1).reshape(1, -1)
    v2 = np.array(emb2).reshape(1, -1)

    similarity = cosine_similarity(v1, v2)[0][0]
    distance = 1.0 - similarity

    return {
        "cosine_similarity": float(similarity),
        "cosine_distance": float(distance)
    }



def chunking(file, chunksize):

    f = open(file)
    filetext = (f.read())
    chunklist = []
    chunks = len(filetext) // chunksize
    # print(chunks, type(chunks))
    currentchunk = 0
    for i in range(chunks):
        chunklist.append(filetext[currentchunk: currentchunk + chunksize])
        currentchunk +=chunksize
    return chunklist



def embeds(text):
    response = client.embeddings.create(
    input= text,
    model="text-embedding-3-large"
    )
    return response.data[0].embedding

alicetext = chunking("alice.txt", 500)[0]

# input = input("What do you want")
# print(embeds(input))




rankings = 3

# for i in range(rankings):
#     textinput = input("What would you like to say?")
#     # textembeds = embeds(textinput)
#     # print(len(textembeds))
#     addtodb(textinput)
    

querytest = input("Say something")

results = collection.query(
    query_texts= querytest, # Chroma will embed this for you
    n_results=rankings # how many results to return
)
print(results)





# inputs = input("What do you want")
# input2 = input("What do you want2")

# embeds1 = embeds(inputs)
# embeds2 = embeds(input2)

# print(embedding_similarity_and_distance(embeds1, embeds2))

# "king" "a male monarch who rules a kingdom"
# "man" "an adult human male"
# "dog" "a domesticated animal kept as a pet"











# response = client.embeddings.create(
#     input= alicetext,
#     model="text-embedding-3-small"
# )

# print(alicetext)
# print(response.data[0].embedding)

# print(len(chunking("alice.txt", 500)))




















