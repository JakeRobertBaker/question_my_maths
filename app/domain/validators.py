from app.domain.exceptions import QuestionParamError


def validate_int(x) -> int:
    # simple validation functin
    # we may do all sorts of strange validation in the domain layer, hence no pydantic.
    if isinstance(x, int):
        return x
    else:
        raise QuestionParamError("Expected Int")
