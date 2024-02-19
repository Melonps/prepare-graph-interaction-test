from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass
class Question:
    questionId: int
    title: str
    description: str
    labels: list[str]
    trueValues: list[int]


@dataclass
class User:
    id: str
    name: str
    questionIdList: list[int]
