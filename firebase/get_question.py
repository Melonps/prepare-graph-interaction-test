import streamlit as st
from google.cloud import firestore

from type import Question


def get_all_collections(db: firestore.Client):
    collections = db.collections()
    collection_names = [collection.id for collection in collections]
    return collection_names


def get_data_from_firestore(db: firestore.Client, collection_name: str):
    docs = db.collection(collection_name).stream()
    data = []
    for doc in docs:
        data.append(doc.to_dict())
    return data


def get_question_from_firestore(question_id: int, db: firestore.Client):
    doc_ref = db.collection("questions").document(str(question_id))
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        question = Question(**data)
        return question
    else:
        st.error("指定された質問が見つかりませんでした。")
