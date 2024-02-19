import streamlit as st

from firebase.clear_data import delete_all_questions
from firebase.get_client import get_db

db = get_db()
st.button("質問を削除する", on_click=delete_all_questions(db))
