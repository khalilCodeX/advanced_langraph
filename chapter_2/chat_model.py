import langchain_openai as ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

def initialize_llm():
    try:
        openai_api_key = os.getenv("OPEN_AI_KEY")
        if openai_api_key is not None:
            llm = ChatOpenAI.ChatOpenAI(
                model="gpt-4o",
                temperature=0.3,
                openai_api_key=openai_api_key,
            )
        else:
            raise ValueError("OPEN_AI_KEY not found in environment variables.")
    except Exception as e:
        print(f"Error initializing ChatOpenAI: {e}")
        llm = None
    return llm