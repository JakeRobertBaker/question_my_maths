from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.base.exceptions import QuestionError
from app.domain.base.topics import Topic


class RegistryDict:
    """Registry keyed by (topic, name), prevents overwrites."""

    def __init__(self):
        self._data: dict[Topic, dict[str, type[Question]]] = {t: {} for t in Topic}

    def add(self, question_cls: type[Question]):
        if not (isinstance(question_cls, type) and issubclass(question_cls, Question)):
            raise QuestionError("Registry can only add Question subclasses")
        topic = question_cls.topic
        name = question_cls.__name__
        if name in self._data[topic]:
            raise QuestionError(
                f"Registry already contains Question '{name}' for topic '{topic.value}'"
            )
        self._data[topic][name] = question_cls

    def get(self, topic: Topic, name: str) -> type[Question]:
        if name not in self._data[topic]:
            raise QuestionError(f"No question '{name}' found for topic '{topic.value}'")
        return self._data[topic][name]

    def get_all(self) -> dict[Topic, dict[str, type[Question]]]:
        return {topic: dict(questions) for topic, questions in self._data.items()}


class Question(ABC):
    topic: Topic
    _registry: RegistryDict = RegistryDict()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Only process concrete classes
        if not hasattr(cls, "__abstractmethods__") or not cls.__abstractmethods__:
            # Validate topic
            if not hasattr(cls, "topic"):
                raise TypeError(f"{cls.__name__} must define a 'topic' class variable")
            if not isinstance(cls.topic, Topic):
                raise TypeError(
                    f"{cls.__name__}.topic must be a Topic enum, got {type(cls.topic)}"
                )

            cls._registry.add(cls)

    @classmethod
    def get_question_class(cls, topic: Topic, name: str) -> type[Question]:
        return cls._registry.get(topic, name)

    @classmethod
    def get_all_questions(cls) -> dict[Topic, dict[str, type[Question]]]:
        return cls._registry.get_all()

    _required_attrs = ("answer", "text")

    def __init__(self, params: dict | None = None):
        self._internal_setup(params)
        missing = [a for a in self._required_attrs if not hasattr(self, a)]
        if missing:
            raise TypeError(
                f"{type(self).__name__}._internal_setup must set: {missing}"
            )

    @abstractmethod
    def _internal_setup(self, params: dict | None = None):
        pass
