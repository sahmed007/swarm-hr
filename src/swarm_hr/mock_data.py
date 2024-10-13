from datetime import datetime, timedelta
from swarm_hr.utils import InterviewerRole, InterviewStage
from enum import Enum


class CandidateStatus(Enum):
    APPLIED = "Applied"
    SHORTLISTED = "Shortlisted"
    REJECTED = "Rejected"
    OFFERED = "Offered"


initial_candidates = [
    (
        "Alice Johnson",
        "alice@example.com",
        "555-123-4567",
        CandidateStatus.OFFERED.value,
    ),
    ("Bob Williams", "bob@example.com", "444-987-6543", CandidateStatus.REJECTED.value),
    ("Emma Brown", "emma@example.com", "777-888-9999", CandidateStatus.APPLIED.value),
    (
        "David Lee",
        "david@example.com",
        "222-333-4444",
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        "Sarah Miller",
        "sarah@example.com",
        "666-555-4444",
        CandidateStatus.APPLIED.value,
    ),
]

now = datetime.now()

initial_interviews = [
    (
        1,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Good communication skills",
        now - timedelta(days=7),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        1,
        InterviewerRole.INTERVIEWER,
        InterviewStage.TECHNICAL_INTERVIEW,
        "Strong technical background",
        now - timedelta(days=3),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        1,
        InterviewerRole.HIRING_MANAGER,
        InterviewStage.FINAL_INTERVIEW,
        "Great cultural fit",
        now - timedelta(days=1),
        CandidateStatus.OFFERED.value,
    ),
    (
        2,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Lack of relevant experience",
        now - timedelta(days=5),
        CandidateStatus.REJECTED.value,
    ),
    (
        3,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Impressive experience",
        now + timedelta(days=1),
        CandidateStatus.APPLIED.value,
    ),
    (
        4,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Good potential",
        now - timedelta(days=2),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        4,
        InterviewerRole.INTERVIEWER,
        InterviewStage.TECHNICAL_INTERVIEW,
        "Solid technical skills",
        now + timedelta(days=2),
        CandidateStatus.SHORTLISTED.value,
    ),
    (
        5,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Interesting background",
        now + timedelta(days=3),
        CandidateStatus.APPLIED.value,
    ),
]
