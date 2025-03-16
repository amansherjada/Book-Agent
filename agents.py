from crewai import Agent

planning_agent = Agent(
    role="Planning Agent",
    goal="Develop the book's concept, outline, characters, and world.",
    backstory="An experienced author specializing in planning and structuring novels.",
    verbose=True
)

writing_agent = Agent(
    role="Writing Agent",
    goal="Write detailed chapters based on the provided outline and character details.",
    backstory="A creative writer adept at bringing stories to life.",
    verbose=True
)

editing_agent = Agent(
    role="Editing Agent",
    goal="Edit the written chapters for clarity, coherence, and grammatical accuracy.",
    backstory="A meticulous editor with an eye for detail.",
    verbose=True
)

fact_checking_agent = Agent(
    role="Fact-Checking Agent",
    goal="Verify the accuracy of all factual information presented in the book.",
    backstory="A diligent researcher ensuring all facts are correct.",
    verbose=True
)

publishing_agent = Agent(
    role="Publishing Agent",
    goal="Format the manuscript and prepare it for publication.",
    backstory="An expert in publishing standards and formatting.",
    verbose=True
)