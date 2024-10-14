from datetime import datetime, timedelta
from swarm_hr.utils import (
    InterviewerRole,
    CandidateStatus,
    INTERVIEWED,
    NOT_INTERVIEWED,
)

initial_candidates = [
    (
        "Alice Johnson",
        "alice@example.com",
        "555-123-4567",
        CandidateStatus.OFFERED.value,
        ["Python", "Java", "SQL", "Project Management"],
    ),
    (
        "Bob Williams",
        "bob@example.com",
        "444-987-6543",
        CandidateStatus.REJECTED.value,
        ["C++", "JavaScript", "React"],
    ),
    (
        "Emma Brown",
        "emma@example.com",
        "777-888-9999",
        CandidateStatus.APPLIED.value,
        ["Ruby", "Rails", "PostgreSQL", "Docker"],
    ),
    (
        "David Lee",
        "david@example.com",
        "222-333-4444",
        CandidateStatus.SHORTLISTED.value,
        ["Python", "Django", "AWS", "Machine Learning"],
    ),
    (
        "Sarah Miller",
        "sarah@example.com",
        "666-555-4444",
        CandidateStatus.APPLIED.value,
        ["JavaScript", "React", "Node.js", "MongoDB"],
    ),
]

now = datetime.now()

initial_interviews = [
    (
        1,
        InterviewerRole.RECRUITER,
        INTERVIEWED,
        "Good communication skills",
        now - timedelta(days=7),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        1,
        InterviewerRole.INTERVIEWER,
        INTERVIEWED,
        "Strong technical background",
        now - timedelta(days=3),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        1,
        InterviewerRole.HIRING_MANAGER,
        INTERVIEWED,
        "Great cultural fit",
        now - timedelta(days=1),
        CandidateStatus.OFFERED.value,
    ),
    (
        2,
        InterviewerRole.RECRUITER,
        INTERVIEWED,
        "Lack of relevant experience",
        now - timedelta(days=5),
        CandidateStatus.REJECTED.value,
    ),
    (
        3,
        InterviewerRole.RECRUITER,
        NOT_INTERVIEWED,
        "Impressive experience",
        now + timedelta(days=1),
        CandidateStatus.APPLIED.value,
    ),
    (
        4,
        InterviewerRole.RECRUITER,
        INTERVIEWED,
        "Good potential",
        now - timedelta(days=2),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        4,
        InterviewerRole.INTERVIEWER,
        NOT_INTERVIEWED,
        "Solid technical skills",
        now + timedelta(days=2),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        5,
        InterviewerRole.RECRUITER,
        NOT_INTERVIEWED,
        "Interesting background",
        now + timedelta(days=3),
        CandidateStatus.APPLIED.value,
    ),
]
