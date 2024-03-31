from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts.chat import (
    ChatPromptTemplate
)
from langchain.vectorstores import FAISS
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
openAI_key = os.environ.get("OPEN_AI")
embeddings = OpenAIEmbeddings()

video_url = "https://www.youtube.com/watch?v=lG7Uxts9SXs&ab_channel=freeCodeCamp.org"

def create_vector_db_from_youtube_url(video_url):
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcript)

    db = FAISS.from_documents(docs, embeddings)
    return db
    # loader = YoutubeLoader.from_youtube_url(video_url)
    # transcript = loader.load()

    # text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    # docs = text_splitter.split_documents(transcript)

    # db = FAISS.from_documents(docs, embeddings)
    # return db

print(create_vector_db_from_youtube_url(video_url))

