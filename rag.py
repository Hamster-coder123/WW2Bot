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





openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                api_key=os.getenv("openaikey"),
                model_name="text-embedding-3-large"
            )
client = chromadb.PersistentClient(path='db')
collection = client.get_or_create_collection(name="HistoryDB", embedding_function=openai_ef)


def addtodb(text, userdata):
    collection.add(ids = [f"{uuid.uuid4()}"],documents = [text], metadatas = [userdata])    



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

# alicetext = chunking("alice.txt", 500)[0]

# input = input("What do you want")
# print(embeds(input))




# rankings = 3

# book1 = addtodb()
    
if(__name__=="__main__"):
    querytest = input("Say something")

    results = collection.query(
        query_texts= querytest, # Chroma will embed this for you
        n_results=2 # how many results to return

    )
    print(results)

def retrieval(prompt, results):
    querytest = prompt

    results = collection.query(
        query_texts= querytest, # Chroma will embed this for you
        n_results=results ,# how many results to return
        include=["documents", "metadatas"]
        
    )
    return results