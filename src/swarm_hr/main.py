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
    You are a recruiter that handles all actions related to screening after a user makes a request.
    You must ask for both the candidate's name and the primary skill they are being screened for. 
    Ask for both name and skill in one message.
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
    You are an in-depth interviewer that handles all actions related to interviewing after a user makes a request.
    You must ask which type of interview is needed, and then ask for the candidate's name.
    The two types of interview choices are technical and behavioral.
    If the interview type is technical, you must ask for two of the primary skills being screened for.
    If the interview type is behavioral, you must ask for a suitable time for the interview.
    """,
    functions=[database.add_interview, database.update_candidate_status],
)

hiring_manager = Agent(
    name="Hiring Manager",
    description=f"""
    You are the hiring manager that handles all actions related to making a shortlist of candidates after a user makes a request.
    You must provide a shortlist of candidates to the user.
    """,
    functions=[database.add_interview, database.update_candidate_status],
)

# Create a routing agent
triage_agent = Agent(
    name="HR Coordinator",
    instructions=f"""
    You are to triage a users request who acts as the hiring manager, and call a tool to transfer to the right intent.
    Once you are ready to transfer to the right intent, call the tool to transfer to the right intent.  
    You dont need to know specifics, just the topic of the request.

    If the user request is about adding a new candidate or performing an initial screening, transfer to the Recruiter.
    If the user request is about adding a new technical interview or behavioral interview, transfer to the Interviewer.
    If the user request is about obtaining a final decision on a candidate or a shortlist, transfer to the Hiring Manager.

    When you need more information to triage the request to an agent, ask a direct question without explaining why you're asking it.
    Do not share your thought process with the user! Do not make unreasonable assumptions on behalf of user.
    """,
    agents=[recruiter, interviewer, hiring_manager],
    add_backlinks=True,
)

if __name__ == "__main__":
    # Run the demo loop
    run_demo_loop(triage_agent, debug=False)
