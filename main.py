from dataclasses import asdict, dataclass

from firebase.add_data import add_question_to_firestore
from firebase.get_client import get_db
from type import Question

db = get_db()


for i in range(1, 21):
    question = Question(
        questionId=i,
        title="インターネット利用率",
        description="これから説明するグラフは都道府県別のインターネット利用率に関するもので、",
        labels=["東京", "大阪", "北海道", "沖縄"],
        trueValues=[53, 50, 49, 48],
    )
    add_question_to_firestore(question, db)
