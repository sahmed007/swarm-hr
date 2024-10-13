import sqlite3
import json
from contextlib import contextmanager
from .mock_data import (
    initial_candidates,
    initial_interviews,
    InterviewerRole,
    InterviewStage,
    CandidateStatus,
)

DB_NAME = "hr_database.db"


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        yield conn
    finally:
        conn.close()


def execute_query(query, params=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.fetchall()


def create_database():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS Candidates (
            candidate_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            status TEXT,
            skills TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS InterviewHistory (
            interview_id INTEGER PRIMARY KEY,
            candidate_id INTEGER,
            scheduled_time TIMESTAMP,
            interviewer TEXT,
            stage TEXT,
            notes TEXT,
            status TEXT,
            FOREIGN KEY (candidate_id) REFERENCES Candidates(candidate_id)
        )
        """,
    ]
    for query in queries:
        execute_query(query)


def add_candidate(name, email, phone, status, skills):
    query = """
    INSERT INTO Candidates (name, email, phone, status, skills)
    VALUES (?, ?, ?, ?, ?)
    """
    skills_json = json.dumps(skills)
    execute_query(query, (name, email, phone, status, skills_json))


def add_interview(
    candidate_id,
    interviewer: InterviewerRole,
    stage: InterviewStage,
    notes,
    scheduled_time=None,
    status=None,
):
    query = """
    INSERT INTO InterviewHistory (candidate_id, scheduled_time, interviewer, stage, notes, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    execute_query(
        query,
        (candidate_id, scheduled_time, interviewer.name, stage.name, notes, status),
    )


def update_candidate_status(candidate_id, new_status: CandidateStatus):
    query = """
    UPDATE Candidates
    SET status = ?
    WHERE candidate_id = ?
    """
    execute_query(query, (new_status.value, candidate_id))


def update_interview_status(interview_id, new_status: CandidateStatus):
    query = """
    UPDATE InterviewHistory
    SET status = ?
    WHERE interview_id = ?
    """
    execute_query(query, (new_status.value, interview_id))


def get_candidate_info(candidate_id):
    query = """
    SELECT * FROM Candidates
    WHERE candidate_id = ?
    """
    result = execute_query(query, (candidate_id,))
    if result:
        candidate = list(result[0])
        candidate[5] = json.loads(candidate[5])
        return tuple(candidate)
    return None


def get_candidate_info_by_name(name):
    query = """
    SELECT * FROM Candidates
    WHERE LOWER(name) LIKE LOWER(?)
    """
    results = execute_query(query, (f"%{name}%",))
    parsed_results = []
    for result in results:
        candidate = list(result)
        candidate[5] = json.loads(candidate[5])
        parsed_results.append(tuple(candidate))
    return parsed_results


def get_interview_history(candidate_id):
    query = """
    SELECT * FROM InterviewHistory
    WHERE candidate_id = ?
    ORDER BY date_of_interview DESC
    """
    return execute_query(query, (candidate_id,))


def preview_table(table_name):
    query = f"SELECT * FROM {table_name} LIMIT 5"
    rows = execute_query(query)
    print(f"\nPreview of {table_name} table:")
    for row in rows:
        print(row)


def initialize_database():
    create_database()

    for candidate in initial_candidates:
        add_candidate(*candidate)

    for interview in initial_interviews:
        add_interview(*interview)
