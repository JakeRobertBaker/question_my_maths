from abc import ABC, abstractmethod


class DomainError(Exception):
    """Base Class for Domain Errors"""


class DomainParamError(DomainError):
    """Base Class for Domain Errors"""


class DomainMissingParams(DomainError):
    """Domain missing params errors"""


class DomainIrrelevantParams(DomainError):
    """Domain missing params errors"""


def validate_int(x) -> int:
    # simple validation functin
    # we may do all sorts of strange validation in the domain layer, hence no pydantic.
    if isinstance(x, int):
        return x
    else:
        raise DomainParamError("Expected Int")


class ParamsDict:
    """Wrapper that tracks which params have been accessed"""

    def __init__(self, params: dict):
        self._params = params.copy()
        self._accessed = set()

    def get(self, key):
        if key not in self._params:
            raise DomainMissingParams(f"Missing required param: {key}")
        self._accessed.add(key)
        return self._params[key]

    def get_unused(self):
        return set(self._params.keys()) - self._accessed


class Params(ABC):
    def __init__(self, params: dict):
        if params:
            wrapped = ParamsDict(params)
            self._validate(wrapped)
            unused = wrapped.get_unused()
            if unused:
                raise DomainIrrelevantParams(f"Unexpected params: {list(unused)}")
        else:
            self._generate()

    @abstractmethod
    def _validate(self, params: ParamsDict):
        """Get and validate params from ParamsDict. Non-mutating."""
        pass

    @abstractmethod
    def _generate(self):
        """Generate params."""
        pass


class Domain(ABC): ...


class ExampleParams(Params):
    def _validate(self, params: ParamsDict) -> None:
        self.m = validate_int(params.get("m"))
        # we may have some strange validation logic
        n = validate_int(params.get("n"))
        if n % self.m == 1:
            self.n = n
        else:
            raise DomainParamError("n must be 1 modulo m")
        # we can add anything but is up to us here to validate.
        self.x: float = params.get("x")

    def _generate(self):
        self.n = 2
        self.m = 3
        self.x = 0.5


class Example(Domain):
    def __init__(self, params: dict):
        self.params = ExampleParams(params)
        self.y = self.params.m + self.params.n
