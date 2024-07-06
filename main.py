from crewai import Crew, Process
from agents import Agents
from tasks import Tasks

agnts = Agents()
tsks = Tasks()

crew = Crew(
    agents=[agnts.researcher(), agnts.writer()],
    tasks=[tsks.task_1(), tsks.task_2()],
    verbose=2,
    process=Process.sequential
)

crew.kickoff()