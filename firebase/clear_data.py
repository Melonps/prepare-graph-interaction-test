from google.cloud import firestore


def delete_all_questions(db: firestore.Client, collection_name: str):
    questions_ref = db.collection(collection_name)
    questions = questions_ref.get()

    if questions:
        for question in questions:
            question.reference.delete()
            print(f"質問 {question.id} を削除しました。")
        print("すべての質問を削除しました。")
    else:
        print("削除する質問が見つかりませんでした。")
