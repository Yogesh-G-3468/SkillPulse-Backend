import os
from dotenv.main import load_dotenv

load_dotenv(dotenv_path = "main_app/.env")
print(os.getenv('MAILPASS'))