from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(
    llm=llm,
)

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
