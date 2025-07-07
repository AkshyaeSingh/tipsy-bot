from dotenv import load_dotenv
import os
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.2)

print(llm.invoke("What's a good drink for summer?"))