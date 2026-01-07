from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
    TEMPERATURE = 0.1

settings = Settings()
