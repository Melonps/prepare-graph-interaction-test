from dataclasses import asdict, dataclass

from firebase.add_data import add_question
from firebase.ger_client import get_db
from type import Question

db = get_db()


for i in range(1, 11):
    queesion = Question(
        question_id=i,
        title="インターネット利用率",
        description="これから説明するグラフは都道府県別のインターネット利用率に関するもので、利用率の大きい順に並んでいます 1位の都道府県から10位の都道府県までを10グループに分割し、1位、2位、3位、4位、5位、6位、7位、8位、9位、10位とします 2位の利用率は1位の9割程度です",
        labels=["東京", "大阪", "北海道", "沖縄"],
        trueValue=[53, 50, 49, 48],
    )
    add_question(queesion, db)
