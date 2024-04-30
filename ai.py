import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv
import os
load_dotenv()

# Access the API key stored in the environment variable
api_key = os.environ.get("API_KEY")

# # Now you can use api_key in your code
# print("API Key:", api_key)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key=api_key)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
    
 
model = genai.GenerativeModel('gemini-pro')
   


response = model.generate_content("What is the meaning of life?")
print((response))
print((response.text))
print(response.candidates[0].content.parts[0].text)