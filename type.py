from dataclasses import dataclass
from datetime import datetime

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
    questionDict: dict
    created_at: datetime
    answer: list[dict] = None
