#from langchain.llms import openai
#from langchain_community.llms import openai
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts.chat import (
    ChatPromptTemplate,
    #HumanMessagePromptTemplate,
    #SystemMessagePromptTemplate,
)
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
openAI_key = os.environ.get("OPEN_AI")

def generate_names(animal_type):
    llm = ChatOpenAI(openai_api_key=openAI_key, 
                     model_name="gpt-3.5-turbo-1106", 
                     temperature=0.6, 
                     max_tokens=512)
    prompt_template = ChatPromptTemplate(
        input_variables=['animal_type'],
        template = "I have a {input_variable} pet and I want good name for it. Suggest 3 names."
    )

    # messages = [
    #     SystemMessage(
    #         content="You are a helpful assistant that gives memorable names."
    #     ),
    #     HumanMessage(
    #         content=prompt_template
    #     ),
    # ]
    chain = LLMChain(llm=llm, prompt=prompt_template)
    response = chain({'animal_type':animal_type})
    return response
    

if __name__ == "__main__":
    res = generate_names("dog")
    print(res)