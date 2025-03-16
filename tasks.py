from crewai import Task
from agents import planning_agent, writing_agent, editing_agent, fact_checking_agent, publishing_agent

tasks = [
    Task(
        description="Develop the book's concept, outline, characters, and world.",
        expected_output="A comprehensive plan including theme, genre, outline, character profiles, and world details.",
        agent=planning_agent
    ),
    Task(
        description="Write detailed chapters based on the provided outline and character details. Each chapter should be at least 1000 words.",
        expected_output="Drafts of all chapters in the book.",
        agent=writing_agent
    ),
    Task(
        description="Edit the written chapters for clarity, coherence, and grammatical accuracy.",
        expected_output="Edited versions of all chapters.",
        agent=editing_agent
    ),
    Task(
        description="Verify the accuracy of all factual information presented in the book.",
        expected_output="A report confirming the accuracy of all facts or detailing necessary corrections.",
        agent=fact_checking_agent
    ),
    Task(
        description="Format the manuscript and prepare it for publication.",
        expected_output="A finalized manuscript ready for publication.",
        agent=publishing_agent
    )
]
