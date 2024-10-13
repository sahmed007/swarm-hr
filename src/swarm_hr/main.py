import os

from dotenv import load_dotenv
from openai import OpenAI
from swarm import Swarm, Agent
from swarm.repl import run_demo_loop
from swarm_hr import database

load_dotenv()

# Create an OpenAI client with the API key
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Pass the OpenAI client to Swarm
client = Swarm(client=openai_client)

# Initialize the database
database.initialize_database()

# Preview tables
database.preview_table("Candidates")
database.preview_table("InterviewHistory")

# Define the agents for each stage of the HR process
recruiter = Agent(
    name="Recruiter",
    description=f"""
    You are an HR recruiter. Introduce the company and position, ask about the candidate's experience and 
    qualifications, and assess their initial fit. If they seem suitable, transfer them to the interviewer.
    """,
    functions=[
        database.add_candidate,
        database.add_interview,
        database.update_candidate_status,
    ],
)

interviewer = Agent(
    name="Interviewer",
    description=f"""
    You are an in-depth interviewer. Ask technical and behavioral questions relevant to the position. 
    If the candidate performs well, transfer them to the hiring manager.
    """,
    functions=[database.add_interview, database.update_candidate_status],
)

hiring_manager = Agent(
    name="Hiring Manager",
    description=f"""
    You are the hiring manager. Review the candidate's performance in previous stages and make a final decision 
    on whether to extend an offer.
    """,
    functions=[database.add_interview, database.update_candidate_status],
)

# Create a routing agent
routing_agent = Agent(
    name="HR Routing Agent",
    instructions=f"""
    You are to route candidates through the appropriate stages of the HR process.
    For new candidates, start with the Recruiter for initial screening.
    If a candidate has passed initial screening, route them to the Interviewer.
    After the interview process is complete, route them to the Hiring Manager for final decision.
    Ensure smooth transitions between stages and maintain the flow of the hiring process.
    Do not share your routing logic with the candidate.
    """,
    agents=[recruiter, interviewer, hiring_manager],
    add_backlinks=True,
)

if __name__ == "__main__":
    # Run the demo loop
    run_demo_loop(routing_agent, debug=False)
