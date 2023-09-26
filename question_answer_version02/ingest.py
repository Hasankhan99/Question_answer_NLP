from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def ingest_data():
    """
    This script ingests Notion data into LangChain. It reads data from a file named 'en_data.txt',
    splits the data into smaller chunks, creates a vector store from the documents, and saves it to disk.
    """
    from pathlib import Path
    from langchain.text_splitter import CharacterTextSplitter
    import faiss
    from langchain.vectorstores import FAISS
    from langchain.embeddings import OpenAIEmbeddings
    import pickle
    import os

    with open ('en_data.txt','r',encoding='utf8') as f:
        data = f.read()

    # Here we split the documents, as needed, into smaller chunks.
    # We do this due to the context limits of the LLMs.
    text_splitter = CharacterTextSplitter(chunk_size=1500, separator="###")
    docs = []
    metadatas = []
    splits = text_splitter.split_text(data)
    docs.extend(splits)
    metadatas.extend([{"source": "en_data.txt"}] * len(splits))

    # Here we create a vector store from the documents and save it to disk.
    store = FAISS.from_texts(docs, OpenAIEmbeddings(), metadatas=metadatas)
    faiss.write_index(store.index, "vector_data/docs.index")
    store.index = None
    with open("vector_data/faiss_store.pkl", "wb") as f:
        pickle.dump(store, f)
