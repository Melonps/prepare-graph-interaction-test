import random
from datetime import datetime

import streamlit as st

from define_question.study3 import get_question_id_list
from firebase.add_data import add_user_to_firestore
from firebase.get_client import get_db
from firebase.get_question import get_all_collections, get_data_from_firestore
from type import User

db = get_db()
# Streamlit アプリのタイトルを設定
st.title("Firebase ユーザーデータ追加アプリ")

# ユーザー情報の入力フォーム
id = st.text_input("IDを入力してください")
db_collection = st.text_input("コレクション名を入力してください")
name = st.text_input("名前を入力してください")

collections = get_all_collections(db)
selected_collection = db_collection

data = get_data_from_firestore(db, db_collection)
# ユーザーデータのプレビュー表示用のエリア
preview_area = st.empty()
n = len(data)  # nを適切な値に設定する
m = 5  # term1とterm2に含まれるサンプルの数
question_num = 30  # 1回のアンケートで出題する質問数

# 1からnまでの乱数データを作成
random_data = random.sample(range(1, n + 1), n)

# term1とterm2のリストを文字列に変換する
question_id_list = get_question_id_list()


# id_list の中身を文字列に変換する
user_data = {
    "ID": id,
    "名前": name,
    "questionDictName": db_collection,
    "questionIdList": question_id_list[:question_num],
    "作成日時": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
}
preview_area.write("以下のデータを送信します:")
preview_area.write(user_data)


if st.button("送信", use_container_width=True, type="primary"):
    user = User(
        id=id,
        name=name,
        questionDictName=db_collection,
        questionIdList=question_id_list[:question_num],
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
