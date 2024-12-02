import os
from dotenv import load_dotenv
load_dotenv(override=True) # loading macros from .env file

class Config:
    ENDPOINT = os.getenv("DOC_ENDPOINT")
    KEY = os.getenv("API_KEY")
    STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")

