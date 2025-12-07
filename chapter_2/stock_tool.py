from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun

def get_stock_price(ticker: str) -> float:
    """Fetches the current stock price for a given ticke symbol. Input should be a 
    valid stock ticker symbol (e.g., 'AAPL' for Apple Inc.). Returns the stock price as a float."""
    ticker_prices = {
        "AAPL": 150.25,
        "GOOGL": 2750.50,
        "MSFT": 299.00,
        "AMZN": 3400.75,
    }
    
    price = ticker_prices.get(ticker.upper())
    if price is None:
        return f"Ticker symbol '{ticker}' not found."
    return price

def prepare_stock_agent(llm):
    search = DuckDuckGoSearchRun()
    tools = [get_stock_price, search]
    system_prompt = ("You are a helpful AI assistant that can fetch stock prices. \
         you have access to the following tools:{tools}" \
        "\n Use the tools to answer the following questions about stock prices\n"
        "if the user asks for a company name, try to infer the ticker symbol. You can use all the tools to do the research and find the reports")

    agent = create_agent(model=llm, system_prompt=system_prompt, tools=tools)
    return agent

def query(agent, question: str):
    print(f"==============Querying stock agent: {question} ======")
    response = agent.invoke({"messages": [{"role": "user", "content": question}]})
    print("Response:")
    print(response["messages"][-1].content)