from enum import Enum, auto


class InterviewerRole(Enum):
    RECRUITER = auto()
    INTERVIEWER = auto()
    HIRING_MANAGER = auto()


class InterviewStage(Enum):
    INITIAL_SCREENING = auto()
    TECHNICAL_INTERVIEW = auto()
    FINAL_INTERVIEW = auto()


initial_candidates = [
    ("Alice Johnson", "alice@example.com", "555-123-4567", "Offer Extended"),
    ("Bob Williams", "bob@example.com", "444-987-6543", "Rejected"),
    ("Emma Brown", "emma@example.com", "777-888-9999", "New"),
]

initial_interviews = [
    (
        1,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Good communication skills",
    ),
    (
        2,
        InterviewerRole.INTERVIEWER,
        InterviewStage.TECHNICAL_INTERVIEW,
        "Strong technical background",
    ),
    (
        3,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Impressive experience",
    ),
    (
        3,
        InterviewerRole.INTERVIEWER,
        InterviewStage.TECHNICAL_INTERVIEW,
        "Knowledge in machine learning",
    ),
    (
        3,
        InterviewerRole.HIRING_MANAGER,
        InterviewStage.FINAL_INTERVIEW,
        "Great cultural fit",
    ),
    (
        4,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Lack of relevant experience",
    ),
    (
        5,
        InterviewerRole.RECRUITER,
        InterviewStage.INITIAL_SCREENING,
        "Scheduled for next week",
    ),
]
