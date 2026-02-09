from abc import ABC, abstractmethod


class DomainError(Exception):
    """Base Class for Domain Errors"""


class DomainParamError(DomainError):
    """Base Class for Domain Errors"""


class DomainMissingParams(DomainError):
    """Domain missing params errors"""


class DomainIrrelevantParams(DomainError):
    """Domain missing params errors"""


def validate_int(x)->int:
    # simple validation functin
    # we may do all sorts of strange validation in the domain layer, hence no pydantic.
    if isinstance(x, int):
        return x
    else:
        raise DomainParamError("Expected Int")


class Params(ABC):
    def __init__(self, params: dict):
        self._validate(params)
        if len(params) > 0:
            raise DomainIrrelevantParams(f"Unexpected params: {list(params.keys())}")

    @abstractmethod
    def _validate(self, params: dict) -> None:
        """Pop and validate params from the dict. Mutates the params dict."""
        pass

class Domain(ABC):...

class ExampleParams(Params):
    def _validate(self, params: dict) -> None:
        self.m = validate_int(params.pop("m"))
        # we may have some strange validation logic
        n = validate_int(params.pop("n"))
        if n % self.m == 1:
            self.n = n
        else:
            raise DomainParamError("n must be 1 modulo m")


class Example(Domain):
    def __init__(self, params:dict):
        self.params = ExampleParams(params)
        self.y = self.params.m + self.params.n
