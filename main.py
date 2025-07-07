# main.py
import os
from langchain.agents import initialize_agent, Tool
from langchain_anthropic import ChatAnthropic
from tools.make_drinks import make_drink
from tools.log_order import log_order

llm = ChatAnthropic(temperature=0.3, model="claude-3-sonnet-20240229")

tools = [
    Tool(name="MakeDrink", func=make_drink, description="Make a drink with a given name for a user."),
    Tool(name="LogOrder", func=log_order, description="Log a drink order to Supabase for analytics."),
]

agent = initialize_agent(tools, llm, agent="chat-zero-shot-react-description", verbose=True)

def run_chat():
    print("Autonomous Bartender Agent is online. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = agent.run(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    run_chat()