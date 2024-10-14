import os

from dotenv import load_dotenv
from openai import OpenAI
from swarm import Swarm, Agent
from swarm.repl import run_demo_loop
from swarm_hr import database, actions

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
    functions=[actions.screen_candidate],
)

interviewer = Agent(
    name="Interviewer",
    description=f"""
    You are an in-depth interviewer that handles all actions related to interviewing after a user makes a request.
    You must ask for the candidate's name along with the job position they are applying for.
    Ask for both name and skill in one message.
    Then you must execute the 'assess_candidate_for_job' function to determine if the candidate is a good fit for the job.
    After the assessment, you must execute the 'mark_candidate_as_interviewed' function to mark the candidate as interviewed.
    """,
    functions=[actions.assess_candidate_for_job, actions.mark_candidate_as_interviewed],
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
hr_coordinator = Agent(
    name="HR Coordinator",
    instructions=f"""
    You are to triage a users request and call a tool to transfer to the right intent.
    Once you are ready to transfer to the right intent, call the tool to transfer to the right intent.  
    You dont need to know specifics, just the topic of the request.

    If the user request is about performing an initial screening, transfer to the Recruiter.
    If the user request is about interviewing a candidate, transfer to the Interviewer.
    If the user request is about obtaining a shortlist, transfer to the Hiring Manager.

    When you need more information to triage the request to an agent, ask a direct question without explaining why you're asking it.
    Do not share your thought process with the user! Do not make unreasonable assumptions on behalf of user.
    """,
    agents=[recruiter, interviewer, hiring_manager],
    add_backlinks=True,
)


def transfer_to_recruiter():
    return recruiter


def transfer_to_interviewer():
    return interviewer


def transfer_to_hiring_manager():
    return hiring_manager


def transfer_to_hr_coordinator():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return hr_coordinator


hr_coordinator.functions = [
    transfer_to_recruiter,
    transfer_to_interviewer,
    transfer_to_hiring_manager,
]
recruiter.functions.append(transfer_to_hr_coordinator)
interviewer.functions.append(transfer_to_hr_coordinator)
# hiring_manager.functions.append(transfer_to_hr_coordinator)

if __name__ == "__main__":
    # Run the demo loop
    run_demo_loop(hr_coordinator, debug=False)
