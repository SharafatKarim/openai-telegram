import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

import openai
openai.api_key = API_KEY

def ai_completion(prompt_text, username):
    # adding a completion
    completion = openai.Completion.create(
        engine="text-davinci-003", 
        prompt = """You're a telegram chatbot named 'Ai Bot BD' built by @sr_tamim (initiator & maintainer) & @SharafatKarim (developer & maintainer).
            """ +  prompt_text + "?", 
        max_tokens=128,
        temperature=0.2,
        user= username
    )
    # print genarated text
    return completion.choices[0].text

def ai_img_generation(prompt_text, username):
    # generating image
    response = openai.Image.create(
        prompt= prompt_text,
        n=1,
        size="1024x1024"
    )
    # get image url from response
    image_url = response['data'][0]['url']
    return image_url