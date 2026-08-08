#print("Hello Python")

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # 환경 변수에서 API 키 가져오기

client = OpenAI(api_key=api_key)  # 오픈AI 클라이언트의 인스턴스 생성

response = client.chat.completions.create(
  model="gpt-4o",
  temperature=0.1,  
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "2022년 월드컵 우승팀은 어디야?"},
  ]		
)

print(response)

print('----')	
print(response.choices[0].message.content) 