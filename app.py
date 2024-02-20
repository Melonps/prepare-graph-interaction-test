import random
from dataclasses import asdict, dataclass
from datetime import datetime

import streamlit as st

from firebase.add_data import add_user_to_firestore
from firebase.get_client import get_db
from type import User

db = get_db()
# Streamlit アプリのタイトルを設定
st.title("Firebase ユーザーデータ追加アプリ")

# ユーザー情報の入力フォーム
id = st.text_input("IDを入力してください")
name = st.text_input("名前を入力してください")

# ユーザーデータのプレビュー表示用のエリア
preview_area = st.empty()
question_id_list_term1 = random.sample(range(1, 11), 5)
question_id_list_term2 = random.sample(range(11, 21), 5)
# id_list の中身を文字列に変換する
question_id_list_term1 = [str(x) for x in question_id_list_term1]
question_id_list_term2 = [str(x) for x in question_id_list_term2]
user_data = {
    "ID": id,
    "名前": name,
    "questionIdList": {
        "term1": question_id_list_term1,
        "term2": question_id_list_term2,
    },
    "作成日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}
preview_area.write("以下のデータを送信します:")
preview_area.write(user_data)


if st.button("送信", use_container_width=True, type="primary"):
    user = User(
        id=id,
        name=name,
        questionDict={
            "term1": question_id_list_term1,
            "term2": question_id_list_term2,
        },
        created_at=datetime.now(),
        answer=[],
    )
    try:
        add_user_to_firestore(
            user=user,
            db=db,
        )
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
