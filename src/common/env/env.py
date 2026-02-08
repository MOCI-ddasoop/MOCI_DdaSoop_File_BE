from dotenv import load_dotenv
import os
from functools import cache

load_dotenv()

def get_env(key:str, default=None) -> str | None:
    return os.environ.get(key, default)

SERVER_URL = get_env("SERVER_URL")