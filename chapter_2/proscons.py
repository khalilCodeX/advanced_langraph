from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

class ProsCons(BaseModel):
    pros: list[str] = Field(description="List of advantages for the given topic")
    cons: list[str] = Field(description="List of disadvantages for the given topic")

def create_proscons_parser():
    parser = JsonOutputParser(pydantic_object=ProsCons)
    print("====== Format Instructions ======")
    print(parser.get_format_instructions())
    print("=================================\n")
    return parser

def chat_prompt_proscons_template(parser):
    chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful AI assistant that specializes that generates pros and cons " \
        "for a given topic.\n Your output must be in valid JSON format conforming to the following schema:\n" \
        "{format_instructions}"),
        ("human","Generate pros and cons for {topic}."),
    ]
    ).partial(format_instructions=parser.get_format_instructions())
    return chat_prompt_template

def format_proscons_output(chain):
    topic = "remote work"
    print(f"==============Generating pros and cons for: {topic} ======")
    response = chain.invoke({"topic": topic})

    print("structured response:")
    print(f"type of response: {type(response)}")

    print(f"pros:")
    for pro in response["pros"]:
        print(f"- {pro}")

    print(f"cons:")
    for con in response["cons"]:
        print(f"- {con}")

    print("raw response:")
    print(response)

