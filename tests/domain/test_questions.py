import pytest

from app.domain.base.exceptions import QuestionParamError
from app.domain.number_theory.questions import Example
from app.domain.linear_algebra.questions import MatrixMult


class TestExample:
    def test_default_construction(self):
        q = Example()
        assert q.answer == 3  # gcd(75, 12) = 3
        assert isinstance(q.text, str)

    def test_explicit_params(self):
        q = Example({"m": 12, "n": 8})
        assert q.answer == 4  # gcd(12, 8) = 4

    def test_invalid_param_type_raises(self):
        with pytest.raises(QuestionParamError):
            Example({"m": "not_int", "n": 8})


class TestMatrixMult:
    def test_default_construction(self):
        q = MatrixMult()
        assert isinstance(q.answer, str)
        assert isinstance(q.text, str)

    def test_explicit_params(self):
        q = MatrixMult({"n": 2, "m": 1})
        assert isinstance(q.answer, str)
        assert "2x2" in q.text

    def test_n_out_of_range_raises(self):
        with pytest.raises(QuestionParamError):
            MatrixMult({"n": 5, "m": 1})

    def test_m_out_of_range_raises(self):
        with pytest.raises(QuestionParamError):
            MatrixMult({"n": 2, "m": 10})
