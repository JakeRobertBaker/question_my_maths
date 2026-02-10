from app.domain.exceptions import QuestionParamError
from app.domain.question_params import Params, ParamsDict
from app.domain.questions import Question
from app.domain.topics import Topic
from app.domain.validators import validate_int
from app.domain.content.number_theory import euclid_alg


class ExampleParams(Params):
    def _validate(self, params: ParamsDict) -> None:
        # can have very simple parameterisation
        self.m: int = validate_int(params.get("m"))
        # we may have some strange validation logic
        n = validate_int(params.get("n"))
        # m cannot divide m and vice versa
        if not (n % self.m != 0) and (self.m % n == 0):
            raise QuestionParamError("n and m cannt divide one another")
        self.n: int = n

    def _generate(self):
        self.m = 75
        self.n = 12


class Example(Question):
    topic = Topic.NUMBER_THEORY

    def _internal_setup(self, params: dict | None = None):
        self.params = ExampleParams(params)
        gcd = euclid_alg(self.params.m, self.params.n)
        self.answer = gcd
        self.text = f"Find the GCD of {self.params.m, self.params.n}"
