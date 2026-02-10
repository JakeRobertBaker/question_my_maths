import pytest

from app.domain.base.exceptions import QuestionError
from app.domain.base.questions import Question
from app.domain.base.topics import Topic
from app.domain.number_theory.questions import Example
from app.domain.linear_algebra.questions import MatrixMult


class TestGetQuestionClass:
    def test_example(self):
        cls = Question.get_question_class(Topic.NUMBER_THEORY, "Example")
        assert cls is Example

    def test_matrix_mult(self):
        cls = Question.get_question_class(Topic.LINEAR_ALGEBRA, "MatrixMult")
        assert cls is MatrixMult

    def test_unknown_name_raises(self):
        with pytest.raises(QuestionError):
            Question.get_question_class(Topic.NUMBER_THEORY, "NonExistent")


class TestGetAllQuestions:
    def test_returns_dict_with_topics(self):
        all_q = Question.get_all_questions()
        assert isinstance(all_q, dict)
        assert Topic.NUMBER_THEORY in all_q
        assert Topic.LINEAR_ALGEBRA in all_q

    def test_contains_registered_questions(self):
        all_q = Question.get_all_questions()
        assert "Example" in all_q[Topic.NUMBER_THEORY]
        assert "MatrixMult" in all_q[Topic.LINEAR_ALGEBRA]
