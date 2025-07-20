from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Generate a detailed report on the following topic: {topic}",
    input_variables=["topic"],
)
# 2nd prompt -> concise report

template2 = PromptTemplate(
    template="Write a five line summary on the following text. \n: {text}",
    input_variables=["text"],
)
prompt1 = template1.invoke({"topic": "The impact of AI on modern society"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt2)
print(result1.content if result1 else "No content generated.")
