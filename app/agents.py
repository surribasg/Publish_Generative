from crewai import Agent

# Market Analyst Agent
analyst_agent = Agent(
    role="Market Analyst",
    goal="Analyze industry trends and detect consumer patterns.",
    backstory="Specialist in financial analysis and trend prediction.",
    llm="ollama/llama3.1"
)

# Marketing Strategist Agent
strategist_agent = Agent(
    role="Marketing Strategist",
    goal="Develop marketing strategies based on market trends.",
    backstory="Expert in advertising strategies and brand positioning.",
    llm="ollama/llama3.1"
)

# Financial Consultant Agent
consultant_agent = Agent(
    role="Financial Consultant",
    goal="Evaluate the economic viability and profitability of strategies.",
    backstory="Financial analyst with experience in investments and risk assessment.",
    llm="ollama/llama3.1"
)
