# --------------------------------GEMINI-------------------------------------

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(model_name='gemini-pro')