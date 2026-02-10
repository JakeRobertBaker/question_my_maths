from random import randint

from app.domain.base.exceptions import QuestionParamError
from app.domain.base.question_params import Params, ParamsDict
from app.domain.base.questions import Question
from app.domain.base.topics import Topic
from app.domain.base.validators import validate_int
from app.domain.linear_algebra.algorithms import symbolic_matrix_power


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
