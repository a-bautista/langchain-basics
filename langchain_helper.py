#from langchain.llms import openai
#from langchain_community.llms import openai
#from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
openAI_key = os.environ.get("OPEN_AI")

def generate_names(translate_text, input_lang, output_lang):
    llm = ChatOpenAI(openai_api_key=openAI_key, 
                     model_name="gpt-3.5-turbo-1106", 
                     temperature=0.6, 
                     max_tokens=512)
    template = (
        "You are a helpful assistant that translates {input_language} to {output_language}."
    )
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    response = llm(
        chat_prompt.format_prompt(
            input_language=input_lang, output_language=output_lang, text=translate_text
        ).to_messages()
    )
    return response
    

if __name__ == "__main__":
    res = generate_names("I love sunsets", "English", "Italian")
    