from enum import Enum, auto


class InterviewerRole(Enum):
    RECRUITER = auto()
    INTERVIEWER = auto()
    HIRING_MANAGER = auto()


class InterviewStage(Enum):
    INITIAL_SCREENING = auto()
    TECHNICAL_INTERVIEW = auto()
    FINAL_INTERVIEW = auto()
