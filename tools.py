from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper
from config import serper_api_key

search = GoogleSerperAPIWrapper(serper_api_key=serper_api_key, type='news')

search_tool = Tool(
    name="Search Google",
    func=search.run,
    description="Tool that allows the agent to search the internet"
)
