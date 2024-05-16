import streamlit as st

from firebase.clear_data import delete_all_questions
from firebase.get_client import get_db
from firebase.get_question import get_all_collections, get_data_from_firestore

db = get_db()
st.title("Firestoreデータ表示アプリ")

# Firestoreから利用可能なコレクション名を取得し、セレクトボックスで表示する
collections = get_all_collections(db)
selected_collection = st.selectbox("コレクションを選択してください:", collections)
if st.button("質問を削除する"):
    delete_all_questions(db, selected_collection)
    st.write("質問を削除しました。")
# 選択されたコレクション内のデータを表示する
if selected_collection:
    data = get_data_from_firestore(db, selected_collection)
    st.write("取得したデータ:")
    for item in data:
        st.write(item)
