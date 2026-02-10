import pytest

from app.domain.base.exceptions import QuestionParamError
from app.domain.base.validators import validate_int


class TestValidateInt:
    def test_valid_int(self):
        assert validate_int(5) == 5

    def test_string_raises(self):
        with pytest.raises(QuestionParamError):
            validate_int("5")

    def test_float_raises(self):
        with pytest.raises(QuestionParamError):
            validate_int(3.14)

    def test_none_raises(self):
        with pytest.raises(QuestionParamError):
            validate_int(None)
