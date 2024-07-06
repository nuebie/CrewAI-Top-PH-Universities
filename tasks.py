from crewai import Task
from agents import Agents

class Tasks:
    def __init__(self):
        self.agents = Agents()
    def task_1(self):
        return Task(
            description = """Use recent data from the web to create a report about the top universities in the Philippines.
                use number and statistics from the web to substantiate the findings of each university.""",
            expected_output = "A comprehensive report about the top universities in the Philippines",
            agent = self.agents.researcher()
        )

    def task_2(self):
        return Task(
            description="""Write a incredibly detailed blog about the top universities in the Philippines using the given report.
                        Use the name of the universities as a header.""",
            expected_output="A blog about top universities in the Philippines",
            agent=self.agents.writer()
        )