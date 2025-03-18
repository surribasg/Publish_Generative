from crewai import Task
from app.agents import analyst_agent, strategist_agent, consultant_agent  # Usamos los mismos nombres

# Task for Market Analyst
analyst_task = Task(
    description="Conduct a detailed market trend analysis.",
    expected_output="A report with insights and detected patterns.",
    agent=analyst_agent
)

# Task for Marketing Strategist
strategist_task = Task(
    description="Develop a marketing strategy based on market trends.",
    expected_output="A marketing plan with clear recommendations.",
    agent=strategist_agent
)

# Task for Financial Consultant
consultant_task = Task(
    description="Evaluate the economic feasibility of the proposed strategies.",
    expected_output="A financial analysis outlining risks and opportunities.",
    agent=consultant_agent
)
