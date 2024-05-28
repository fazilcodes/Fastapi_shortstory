# from openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a short story creator expert about a character and its details and the story must be 4 to 5 sentence maximum"},
#         {"role": "user", "content": "character name is Jaggu and the details is Monkey who is friends with people and loves eating laddu"}
#     ]
# )

# print(completion)

# --------------------------------GEMINI-------------------------------------

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(model_name='gemini-pro')