from dataclasses import dataclass

from dataclasses_json import dataclass_json


@dataclass
class Question:
    question_id: int
    title: str
    description: str
    labels: list[str]
    trueValue: list[int]


@dataclass
class User:
    id: str
    name: str
    question_id_list: list[int]
