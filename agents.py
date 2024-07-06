from crewai import Agent
from model import Model
from tools import search_tool
from config import local_model

class Agents:
    def researcher(self):
        return Agent(
            role = 'Researcher',
            goal = """
                Do a comprehensive research about the top universities in the Philippines at 2024. Include the
                strengths and weaknesses of each university. Provide reasons why someone should or should not study 
                in each university. Use number and statistics to substantiate your research.
                """,
            backstory = """
                You are a well trusted AI research assistant that uses factual data and multiple sources from the web to
                create well-detailed and truthful reports about the top universities in the Philippines.
                """,
            verbose = True,
            llm = Model(local_model).model,
            tools = [search_tool],
            allow_delegation = False
        )

    def writer(self):
        return Agent(
            role = 'Writer',
            goal = """
                Write a detailed blog about the top universities in the Philippines using the findings of the 
                researcher. Make sure to include the important details in the blog.
                """,
            backstory = """
                You are a AI writer than uses the research findings of the researcher to create detailed and organized
                blogs.
                """,
            verbose = True,
            llm = Model(local_model).model,
            allow_delegation=False
        )