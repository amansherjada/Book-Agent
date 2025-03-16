from crewai import Crew, Process, LLM
from agents import planning_agent, writing_agent, editing_agent, fact_checking_agent, publishing_agent
from tasks import tasks
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the Groq API key from environment variables
# groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Initialize the Groq LLM
# llm = LLM(
#     model="groq/llama-3.3-70b-versatile", 
#     api_key=groq_api_key,
#     temperature=0.5,  # Adjust the temperature for response variability
#     max_completion_tokens=1024,  # Set the maximum number of tokens in the response
#     top_p=0.9,  # Set the nucleus sampling parameter
#     stop=None,  # Define stop sequences if needed
#     stream=False  # Enable streaming if supported
# )

# Initialize the Gemini LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=google_api_key,
    temperature=0.5,  # Adjust the temperature for response variability
    max_completion_tokens=1024,  # Set the maximum number of tokens in the response
    top_p=0.9,  # Set the nucleus sampling parameter
    stop=None,  # Define stop sequences if needed
    stream=False  # Enable streaming if supported
)

planning_agent.llm = llm
writing_agent.llm = llm
editing_agent.llm = llm
fact_checking_agent.llm = llm
publishing_agent.llm = llm

# Create the Crew instance with agents and tasks
book_writing_crew = Crew(
    agents=[planning_agent, writing_agent, editing_agent, fact_checking_agent, publishing_agent],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    # Run the Crew instance
    # Execute the workflow
    result = book_writing_crew.kickoff()

    # Define the file path
    output_file = "final_manuscript.md"  # Change to .txt if needed

    # Save the output to a Markdown file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("# Final Manuscript\n\n")  # Markdown Header
        file.write(str(result))  # Convert CrewOutput to string

    print(f"Final Manuscript saved to {output_file}")