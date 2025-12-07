from chat_model import initialize_llm
from proscons import create_proscons_parser, chat_prompt_proscons_template, format_proscons_output
from books import create_books_parser, chat_prompt_books_template, format_books_output
from stock_tool import prepare_stock_agent, query

llm = initialize_llm()
if llm is None:
    raise ValueError("Failed to initialize the language model.")

#parser = create_proscons_parser()
#parser = create_books_parser()

#prompt = chat_prompt_proscons_template(parser)
#prompt = chat_prompt_books_template(parser)

#chain = prompt | llm | parser

#format_proscons_output(chain)
#format_books_output(chain)

agent = prepare_stock_agent(llm)
question = "What is the current stock price of Apple?"
query(agent, question)

question = "What is the current stock price of Goog?"
query(agent, question)

question = "What is the current stock price of XYZCorp?"
query(agent, question)

question = "Summarize the key findings of the latest stock report on MSFT."
query(agent, question)