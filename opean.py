import openai
import os
from dotenv import load_dotenv


def get_openai_response(prompt,filter):
    # Set your OpenAI API key
    load_dotenv()

    # Access the API key stored in the environment variable
    api_key = os.environ.get("OPEN_AI_KEY")
    openai.api_key = api_key
    
    if(filter=="true"):
      print(filter)
      reframe_prompt = "Check what is vulgar word in this prompt provided  if yes then reframe if no generally provide same content "+prompt
    else:
       print(filter)
       reframe_prompt="Generate Beautiful blog provided in this prompt within 150 words only with complete sense. "+prompt
       
    
    
   
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": reframe_prompt}],
        max_tokens=200
    )

    # Get the generated text from the response
    generated_text = response['choices'][0]['message']['content']
    return generated_text
