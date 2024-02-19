from dataclasses import asdict, dataclass

import streamlit as st

from type import Question, User


def add_question_to_firestore(question: Question, db):
    db.collection("questions").document(str(question.questionId)).set(asdict(question))


# データを Firestore に追加する関数
def add_user_to_firestore(user: User, db):
    db.collection("users").document(str(user.id)).set(asdict(user))
    st.success("ユーザーデータが追加されました！")
