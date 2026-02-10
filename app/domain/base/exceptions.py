class QuestionError(Exception):
    """Base Class for Question Errors"""


class QuestionParamError(QuestionError):
    """Base Class for Question Errors"""


class QuestionMissingParams(QuestionError):
    """Question missing params errors"""


class QuestionIrrelevantParams(QuestionError):
    """Question missing params errors"""
