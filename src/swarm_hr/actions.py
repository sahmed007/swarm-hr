from .database import execute_query, get_candidate_info_by_name
from .utils import INTERVIEWED
from .external import assess_candidate_fit
import json
from .mock_data import InterviewerRole, CandidateStatus


def screen_candidate(candidate_name: str, skill: str) -> bool:
    """
    Screen a candidate based on their name and a specific skill.
    Args:
        candidate_name (str): The name of the candidate to screen.
        skill (str): The skill to check for in the candidate's skill set.
    """
    query = """
    SELECT skills FROM Candidates
    WHERE LOWER(name) LIKE LOWER(?)
    """
    results = execute_query(query, (f"%{candidate_name}%",))

    for result in results:
        skills = json.loads(result[0])
        if skill.lower() in [s.lower() for s in skills]:
            return True

    return False


def mark_candidate_as_interviewed(
    candidate_name: str, notes: str = "Candidate was interviewed."
) -> bool:
    """
    Mark a candidate as interviewed by adding a new entry to the InterviewHistory table.

    Args:
        candidate_name (str): The name of the candidate to mark as interviewed.
        interviewer (InterviewerRole): The role of the interviewer.
        notes (str, optional): Any notes from the interview. Defaults to an empty string.
    """
    candidate_info = get_candidate_info_by_name(candidate_name)
    if not candidate_info:
        return False

    candidate_id = candidate_info[0][0]

    query = """
    INSERT INTO InterviewHistory (candidate_id, interviewer, interviewed, notes, status)
    VALUES (?, ?, ?, ?, ?)
    """
    execute_query(
        query,
        (
            candidate_id,
            InterviewerRole.INTERVIEWER.value,
            INTERVIEWED,
            notes,
            CandidateStatus.APPLIED.value,
        ),
    )

    return True


def assess_candidate_for_job(candidate_name: str, job_position: str) -> bool:
    """
    Assess a candidate's fit for a specific job position based on their skills.

    Args:
        candidate_name (str): The name of the candidate to assess.
        job_position (str): The job position to assess the candidate for.
    """
    query = """
    SELECT skills FROM Candidates
    WHERE LOWER(name) LIKE LOWER(?)
    """
    results = execute_query(query, (f"%{candidate_name}%",))

    if not results:
        return False

    candidate_skills = json.loads(results[0][0])
    is_good_fit = assess_candidate_fit(candidate_skills, job_position)

    return is_good_fit


def get_shortlist() -> list[str]:
    """
    Get a shortlist of candidates from the Candidates table.
    """
    query = """
    SELECT name FROM Candidates
    WHERE LOWER(status) = LOWER(?)
    """
    results = execute_query(query, (CandidateStatus.SHORTLISTED.value,))
    candidates = [result[0] for result in results]

    return candidates
