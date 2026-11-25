import json
from pydantic import BaseModel,Field
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_KEY = os.getenv('GEMINI_KEY')

client = genai.Client(api_key=GEMINI_KEY)

# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=[
#         {'role':'user' , 'parts':[{'text':'what is llm?'}]},
#         {'role':'model' , 'parts':[{'text':' LLM stands for Large Language Model.'}]},
#         {'role':'user' , 'parts':[{'text':'what is llm?'}]}
#     ]
# )
# print(response.text)

# res1=client.models.generate_content(
#     model="gemini-2.5-flash",
    
#     contents="What is square root of 9",
#     config={
#         "system_instruction":"You are a mathematician who cracks jokes and answer",
#         "temperature": 0.8,
#         "max_output_tokens": 100
#     }
# )
# print(res1.text)
# print(res1.usage_metadata.prompt_token_count)
# print(res1.usage_metadata.candidates_token_count)


# res2=client.models.generate_content_stream(
#     model="gemini-2.5-flash",
#     contents="tell me the story of sinbaad"
# )
# for chunk in res2:
#     print(chunk.text,end="")

# 

# class Person(BaseModel):
#     name: str
#     age: int
#     city: str

# result = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents="Give me the name, age and city of a fictional person.",
#     config={
#         "system_instruction": "You are a helpful assistant.",
#         "response_mime_type": "application/json",
#         "response_schema": Person,
#     }
# )

# person = Person.model_validate_json(result.text)
# print(person)
# print(person.name)
# print(person.age)
# print(person.city)


# Step 1: Define your function
def weather(city: str):
     """Get the current weather for a given city."""
     return {
          "name": city,
          "temprature": "28",
          "degree": "Celcius",
          "weather": "Sunny"
     }

# Step 2: Describe the function to the model (the tool definition)
from google.genai import types

weather_tool = types.Tool(
     function_declarations=[
          types.FunctionDeclaration(
               name="weather",
               description="Get the current weather for a given city",
               parameters=types.Schema(
                    type="OBJECT",
                    properties={
                         "city": types.Schema(
                              type="STRING",
                              description="The city to get weather for"
                         )
                    },
                    required=["city"]
               )
          )
     ]
)

# Step 3: Send the query with the tool
response = client.models.generate_content(
     model="gemini-2.5-flash",
     contents="weather of Pune city?",
     config={
          "system_instruction": "You are a weather expert",
          "tools": [weather_tool],
     }
)
print(response.text)