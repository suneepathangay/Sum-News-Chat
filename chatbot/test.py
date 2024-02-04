from hugchat import hugchat
from hugchat.login import Login
import os
from dotenv import load_dotenv

load_dotenv()

sign = Login(os.getenv('HUGGING_FACE_USER'), os.getenv('HUGGING_FACE_PASS'))
cookies = sign.login()

chatbot = hugchat.ChatBot(cookies=cookies.get_dict()) 
query_result = chatbot.query("Tell me about yourself!")
print(query_result)