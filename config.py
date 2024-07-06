from dotenv import load_dotenv
import os

load_dotenv()

local_model = os.getenv('MODEL')
serper_api_key = os.getenv('SERPER_API_KEY')