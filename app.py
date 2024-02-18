import random
from dataclasses import asdict, dataclass

import streamlit as st

from firebase.add_data import add_user_to_firestore
from firebase.ger_client import get_db
from type import User

db = get_db()
# Streamlit アプリのタイトルを設定
st.title("Firebase ユーザーデータ追加アプリ")

# ユーザー情報の入力フォーム
id = st.text_input("IDを入力してください")  # <- Id を id に変更
name = st.text_input("名前を入力してください")


# 追加ボタンが押されたときの処理
if st.button("ユーザーデータを追加"):
    question_id_list = random.sample(range(1, 11), 5)
    user = User(id=id, question_id_list=question_id_list)
    add_user_to_firestore(user=user, name=name, db=db)
