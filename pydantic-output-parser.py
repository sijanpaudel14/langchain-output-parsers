import time
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# ✅ Clear terminal (only for Unix-like systems)
if os.name == "posix":
    os.system("clear")

# ✅ Load .env environment variables
load_dotenv()

# ✅ Start timer
start_time = time.time()

# ✅ Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# ✅ Define a Pydantic model


class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(..., description="The city where the person lives")


# ✅ Create output parser using the Person model
parser = PydanticOutputParser(pydantic_object=Person)

# ✅ Create the prompt template
template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person.\n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# ✅ Chain the model, template, and parser
chain = template | model | parser

# ✅ Invoke the chain
try:
    result = chain.invoke({"place": "Nepalese"})
    print(result)
except Exception as e:
    print("❌ Error during model invocation:", e)

# ✅ End timer
end_time = time.time()
print(f"\n⏱️  Time taken: {end_time - start_time:.4f} seconds")
