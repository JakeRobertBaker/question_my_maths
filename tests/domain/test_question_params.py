import pytest

from app.domain.base.exceptions import QuestionIrrelevantParams, QuestionMissingParams
from app.domain.base.question_params import Params, ParamsDict


class TestParamsDict:
    def test_get_returns_value_and_tracks_access(self):
        pd = ParamsDict({"a": 1, "b": 2})
        assert pd.get("a") == 1
        assert pd.get_unused() == {"b"}

    def test_get_missing_key_raises(self):
        pd = ParamsDict({"a": 1})
        with pytest.raises(QuestionMissingParams):
            pd.get("missing")

    def test_get_unused_returns_unaccessed_keys(self):
        pd = ParamsDict({"a": 1, "b": 2, "c": 3})
        pd.get("a")
        pd.get("c")
        assert pd.get_unused() == {"b"}


class _ConcreteParams(Params):
    """Minimal concrete Params for testing."""

    def _validate(self, params: ParamsDict):
        self.x = params.get("x")

    def _generate(self):
        self.x = 42


class TestParams:
    def test_extra_keys_raises(self):
        with pytest.raises(QuestionIrrelevantParams):
            _ConcreteParams({"x": 1, "extra": 99})

    def test_none_params_calls_generate(self):
        p = _ConcreteParams(None)
        assert p.x == 42

    def test_no_args_calls_generate(self):
        p = _ConcreteParams()
        assert p.x == 42

    def test_valid_params_accepted(self):
        p = _ConcreteParams({"x": 7})
        assert p.x == 7
