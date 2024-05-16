import streamlit as st

from firebase.add_data import add_user_to_firestore
from firebase.get_client import get_db
from firebase.get_question import get_all_collections, get_data_from_firestore
from type import User

db = get_db()

id = st.text_input("IDを入力してください")


data = get_data_from_firestore(db, "users")
# ユーザーデータのプレビュー表示用のエリア
st.write(data)
