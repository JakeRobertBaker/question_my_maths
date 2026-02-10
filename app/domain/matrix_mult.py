from random import randint

from app.domain.exceptions import QuestionParamError
from app.domain.question_params import Params, ParamsDict
from app.domain.questions import Question
from app.domain.topics import Topic
from app.domain.validators import validate_int
from app.domain.content.linear_algebra import symbolic_matrix_power


class MatrixMultParams(Params):
    def _validate(self, params: ParamsDict) -> None:
        n = validate_int(params.get("n"))
        if not 1 <= n <= 3:
            raise QuestionParamError("n must be between 1 and 3")
        self.n: int = n

        m = validate_int(params.get("m"))
        if not 1 <= m <= 3:
            raise QuestionParamError("m must be between 1 and 3")
        self.m: int = m

    def _generate(self):
        self.n = randint(1, 3)
        self.m = randint(1, 3)


class MatrixMult(Question):
    topic = Topic.LINEAR_ALGEBRA

    def _internal_setup(self, params: dict | None = None):
        self.params = MatrixMultParams(params)
        self.answer = symbolic_matrix_power(self.params.n, self.params.m)
        self.text = (
            f"Compute X^{self.params.m} for a {self.params.n}x{self.params.n} "
            f"symbolic matrix X"
        )
