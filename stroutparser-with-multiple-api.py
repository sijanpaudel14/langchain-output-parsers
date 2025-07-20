from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from keys import API_KEYS  # Assuming API_KEYS is defined in keys.py
import os
os.system('clear')
load_dotenv()


# Prompts and parser
template1 = PromptTemplate(
    template="Generate a detailed report on the following topic: {topic}",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="Write a five line summary on the following text. \n: {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

def try_chain_with_keys(topic: str):
    for key in API_KEYS:
        try:
            model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=key)
            chain = template1 | model | parser | template2 | model | parser
            result = chain.invoke({"topic": topic})
            return result
        except Exception as e:
            print(f"⚠️  Failed with key {key[:6]}... Trying next. Error: {str(e)[:100]}")
    raise RuntimeError("❌ All API keys failed or quota exceeded.")

# Use it
topic = "The impact of AI on modern society"
result = try_chain_with_keys(topic)
print(result if result else "No content generated.")
