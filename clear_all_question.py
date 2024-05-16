import argparse

from firebase.clear_data import delete_all_questions
from firebase.get_client import get_db

db = get_db()
delete_all_questions(db, argparse.collection_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection_name", type=str, default="questions")
    print("clear_all_question.py was executed.")
