import time
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
import os
os.system('clear')
load_dotenv()

time1 = time.time()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

schema = [ResponseSchema(name="fact 1", description="Fact 1 about the topic",),
          ResponseSchema(name="fact 2", description="Fact 2 about the topic",),
          ResponseSchema(name="fact 3", description="Fact 3 about the topic",)
          ]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Generate three facts about the topic: {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({"topic": "The impact of AI on modern society"})

print(result)
print(f"\nFact 1: {result['fact 1']}\n")
print(f"Fact 2: {result['fact 2']}\n")
print(f"Fact 3: {result['fact 3']}\n")
time2 = time.time()
print(f"Time taken: {round(time2 - time1, 2)} seconds")
