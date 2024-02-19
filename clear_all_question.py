from firebase.clear_data import delete_all_questions
from firebase.get_client import get_db

db = get_db()
delete_all_questions(db)
