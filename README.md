# 🔍 LangChain Output Parsers

A comprehensive collection of LangChain output parser implementations demonstrating various techniques for structured data extraction from Language Models.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Output Parser Types](#output-parser-types)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage Examples](#usage-examples)
- [Files Description](#files-description)
- [Key Concepts](#key-concepts)
- [Best Practices](#best-practices)

## 🎯 Overview

This repository contains practical implementations of different LangChain output parsers that help structure and format responses from Language Models. Each implementation demonstrates a specific parsing technique with real-world examples.

## ✨ Features

- **Multiple Output Parser Types**: JSON, Pydantic, Structured, and String parsers
- **Model Integration**: Google Generative AI (Gemini) and HuggingFace models
- **Error Handling**: Robust error handling with fallback mechanisms
- **Performance Monitoring**: Built-in timing for performance analysis
- **API Key Management**: Multiple API key rotation for quota management
- **Chain Operations**: Sequential model operations with different parsers

## 🔧 Output Parser Types

### 1. **Pydantic Output Parser** 📝

- Uses Pydantic models for strong type validation
- Automatic field validation and constraints
- Structured data with field descriptions

### 2. **JSON Output Parser** 🔗

- Simple JSON format output
- Direct dictionary access to parsed data
- Flexible structure handling

### 3. **Structured Output Parser** 📊

- Schema-based parsing with ResponseSchema
- Multiple facts or data points extraction
- Organized data presentation

### 4. **String Output Parser** 📄

- Basic string processing and chaining
- Multiple API integration support
- Sequential prompt processing

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/sijanpaudel14/langchain-output-parsers.git
cd langchain-output-parsers

# Install required packages
pip install -r requirements.txt
```

### Required Dependencies

```txt
langchain-core
langchain-google-genai
langchain-huggingface
pydantic
python-dotenv
```

## 🔐 Environment Setup

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_API_KEY_1=backup_key_1
GOOGLE_API_KEY_2=backup_key_2
GOOGLE_API_KEY_3=backup_key_3
GOOGLE_API_KEY_4=backup_key_4
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

## 📖 Usage Examples

### Pydantic Output Parser Example

```python
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

class Person(BaseModel):
    name: str = Field(..., description="The name of the person")
    age: int = Field(gt=18, description="The age of the person")
    city: str = Field(..., description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)
chain = template | model | parser
result = chain.invoke({"place": "Nepalese"})
```

### JSON Output Parser Example

```python
from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()
chain = template | model | parser
result = chain.invoke({})
print(result['name'])  # Direct dictionary access
```

### Structured Output Parser Example

```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

schema = [
    ResponseSchema(name="fact 1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact 2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact 3", description="Fact 3 about the topic")
]
parser = StructuredOutputParser.from_response_schemas(schema)
```

## 📁 Files Description

| File                                | Description                                  | Key Features                                   |
| ----------------------------------- | -------------------------------------------- | ---------------------------------------------- |
| `pydantic-output-parser.py`         | Pydantic model-based parsing with validation | Type safety, field constraints, error handling |
| `jsonoutputparser.py`               | Simple JSON format output parsing            | Direct dictionary access, flexible structure   |
| `structuredoutputparser.py`         | Schema-based structured data extraction      | Multiple facts, organized output, timing       |
| `stroutputparser.py`                | Basic string output processing               | Google GenAI integration, simple chaining      |
| `stroutputparser_genai.py`          | Enhanced string parser with GenAI            | Sequential prompts, detailed reports           |
| `stroutparser-with-multiple-api.py` | Multi-API key rotation system                | Fallback mechanism, quota management           |
| `keys.py`                           | API key management utility                   | Multiple key storage, environment loading      |

## 💡 Key Concepts

### 1. **Output Parser Chain Pattern**

```python
chain = template | model | parser
result = chain.invoke(input_data)
```

### 2. **Format Instructions**

All parsers provide format instructions that guide the model:

```python
partial_variables={"format_instructions": parser.get_format_instructions()}
```

### 3. **Error Handling**

```python
try:
    result = chain.invoke({"place": "Nepalese"})
    print(result)
except Exception as e:
    print("❌ Error during model invocation:", e)
```

### 4. **Performance Monitoring**

```python
start_time = time.time()
# ... processing ...
end_time = time.time()
print(f"⏱️  Time taken: {end_time - start_time:.4f} seconds")
```

### 5. **API Key Rotation**

```python
def try_chain_with_keys(topic: str):
    for key in API_KEYS:
        try:
            model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=key)
            return chain.invoke({"topic": topic})
        except Exception as e:
            print(f"⚠️  Failed with key {key[:6]}... Trying next.")
```

## 🎯 Best Practices

### 1. **Model Selection**

- Use `gemini-2.0-flash` for fast responses
- Consider `gemini-pro` for complex tasks
- HuggingFace models for specific use cases

### 2. **Template Design**

- Clear and specific instructions
- Include format instructions for parsers
- Use descriptive input variables

### 3. **Error Handling**

- Always wrap model invocations in try-catch blocks
- Implement fallback mechanisms for API failures
- Log errors for debugging

### 4. **Performance Optimization**

- Monitor execution time
- Use appropriate model sizes
- Cache results when possible

### 5. **Security**

- Store API keys in environment variables
- Use `.gitignore` to exclude sensitive files
- Implement key rotation for quota management

## 🚀 Getting Started

1. **Clone the repository**
2. **Set up your environment variables**
3. **Install dependencies**
4. **Run any of the example files**:

```bash
python pydantic-output-parser.py
python jsonoutputparser.py
python structuredoutputparser.py
```

## 🔮 Advanced Features

- **Sequential Chaining**: Connect multiple models and parsers
- **Multi-API Support**: Automatic fallback between different API keys
- **Validation**: Strong type checking with Pydantic models
- **Structured Data**: Extract multiple data points with schemas
- **Performance Metrics**: Built-in timing and monitoring

## 🤝 Contributing

Feel free to contribute by:

- Adding new output parser implementations
- Improving error handling
- Adding more model integrations
- Enhancing documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Parsing! 🎉**

_Built with ❤️ using LangChain and various Language Models_
