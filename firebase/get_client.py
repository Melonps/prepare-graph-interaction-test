import json
import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app

# .envファイルから環境変数を読み込む
load_dotenv()


def get_db():

    # 初期化されていない場合は初期化を行う
    if not firebase_admin._apps:
        with open("./service_account_key.json", "r") as f:
            firebase_service_account_key = json.load(f)
        # Firebase Admin SDKの初期化
        cred = credentials.Certificate(firebase_service_account_key)
        initialize_app(cred)

    # Firestoreクライアントの作成
    db = firestore.client()
    return db
