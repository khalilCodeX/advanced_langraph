from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class books(BaseModel):
    title: str = Field(description="Title of the book")
    ingredients: list[str] = Field(description="List of ingredients for the given book")
    description: list[str] = Field(description="List of steps to complete the recipe using the ingredients")

def create_books_parser():
    parser = JsonOutputParser(pydantic_object=books)
    print("====== Format Instructions ======")
    print(parser.get_format_instructions())
    print("=================================\n")
    return parser

def chat_prompt_books_template(parser):
    chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful AI assistant that specializes that generates list of ingredients and \
         steps to make itgiven a dish" \
        "\n Your output must be in valid JSON format conforming to the following schema:\n" \
        "{format_instructions}"),
        ("human","Generate title, ingredients and descriptions for {topic}."),
    ]
    ).partial(format_instructions=parser.get_format_instructions())
    return chat_prompt_template

def format_books_output(chain):
    topic = "chicken biryani"
    print(f"==============Generating title, ingredients and descriptions for: {topic} ======")
    response = chain.invoke({"topic": topic})

    print("structured response:")
    print(f"type of response: {type(response)}")

    print(f"Title:")
    print(f"- {response['title']}")

    print(f"Ingredients:")
    for ingredient in response["ingredients"]:
        print(f"- {ingredient}")

    print(f"Descriptions:")
    for description in response["description"]:
        print(f"- {description}")

    print("raw response:")
    print(response)



