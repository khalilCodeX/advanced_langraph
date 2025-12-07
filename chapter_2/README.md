# Chapter 2: LangChain Output Parsing & Tool Agents

This chapter demonstrates key LangChain concepts including structured output parsing with Pydantic models, prompt templates, and building tool-enabled agents.

## 📚 What You'll Learn

### 1. **Structured Output Parsing with Pydantic**
Learn how to use `JsonOutputParser` with Pydantic models to get structured, validated JSON responses from LLMs.

- **Files**: `proscons.py`, `books.py`
- **Key Concepts**:
  - Defining Pydantic models with `Field` descriptions
  - Using `JsonOutputParser` to parse LLM outputs
  - Format instructions that guide the LLM to produce valid JSON

### 2. **Chat Prompt Templates**
Learn how to create reusable prompt templates with system and human message patterns.

- **Key Concepts**:
  - `ChatPromptTemplate.from_messages()` for multi-turn conversations
  - Using `.partial()` to inject format instructions
  - Template variables like `{topic}` and `{format_instructions}`

### 3. **LangChain Expression Language (LCEL) Chains**
Understand how to compose LLM pipelines using the `|` operator.

- **File**: `chat.py`
- **Key Concepts**:
  - Building chains: `prompt | llm | parser`
  - Invoking chains with input dictionaries

### 4. **Tool-Enabled Agents**
Build agents that can use external tools to answer questions.

- **File**: `stock_tool.py`
- **Key Concepts**:
  - Creating custom tools (functions with docstrings)
  - Integrating search tools (`DuckDuckGoSearchRun`)
  - Using `create_agent` to build a tool-calling agent
  - System prompts that guide tool usage

## 🗂️ File Overview

| File | Description |
|------|-------------|
| `chat_model.py` | LLM initialization with OpenAI GPT-4o |
| `proscons.py` | Pros/Cons generator with structured output |
| `books.py` | Recipe generator with structured output |
| `stock_tool.py` | Stock price agent with custom tools |
| `chat.py` | Main entry point that ties everything together |

## 🚀 Getting Started

### Prerequisites

1. **Python 3.10+** installed
2. **OpenAI API Key** set in your environment

### Installation

```bash
# Install required packages
pip install langchain langchain-openai langchain-community pydantic python-dotenv duckduckgo-search
```

### Environment Setup

Create a `.env` file in the project root:

```env
OPEN_AI_KEY=your_openai_api_key_here
```

### Running the Examples

```bash
# Navigate to the chapter directory
cd advanced_langraph/chapter_2

# Run the main chat script
python chat.py
```

## 💡 Example Usage

### Structured Output (Pros/Cons)

```python
from chat_model import initialize_llm
from proscons import create_proscons_parser, chat_prompt_proscons_template

llm = initialize_llm()
parser = create_proscons_parser()
prompt = chat_prompt_proscons_template(parser)
chain = prompt | llm | parser

response = chain.invoke({"topic": "remote work"})
# Returns: {"pros": [...], "cons": [...]}
```

### Stock Agent Query

```python
from chat_model import initialize_llm
from stock_tool import prepare_stock_agent, query

llm = initialize_llm()
agent = prepare_stock_agent(llm)
query(agent, "What is the current stock price of Apple?")
```

## 🧠 Key Takeaways

1. **Pydantic + JsonOutputParser** = Reliable structured outputs from LLMs
2. **Format Instructions** tell the LLM exactly what JSON schema to follow
3. **LCEL Chains** make it easy to compose prompt → LLM → parser pipelines
4. **Agents with Tools** can perform actions like searching or fetching data
5. **System Prompts** guide agent behavior and tool usage

## 📖 Further Learning

- [LangChain Documentation](https://python.langchain.com/docs/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [LangChain Output Parsers](https://python.langchain.com/docs/concepts/output_parsers/)
- [LangChain Agents](https://python.langchain.com/docs/concepts/agents/)

---

Happy coding! 🎉
