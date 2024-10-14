from enum import Enum, auto


class InterviewerRole(Enum):
    RECRUITER = auto()
    INTERVIEWER = auto()
    HIRING_MANAGER = auto()


class CandidateStatus(Enum):
    APPLIED = "Applied"
    SHORTLISTED = "Shortlisted"
    REJECTED = "Rejected"
    OFFERED = "Offered"


INTERVIEWED = True
NOT_INTERVIEWED = False
