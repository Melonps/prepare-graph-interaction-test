import json
import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からFirebaseの秘密鍵情報(JSON文字列)を取得し、辞書に変換
firebase_service_account_key_str = os.getenv("FIREBASE_SERVICE_ACCOUNT_KEY")


def get_db():

    # 初期化されていない場合は初期化を行う
    if not firebase_admin._apps:
        firebase_service_account_key = json.loads(firebase_service_account_key_str)
        # Firebase Admin SDKの初期化
        cred = credentials.Certificate(firebase_service_account_key)
        initialize_app(cred)

    # Firestoreクライアントの作成
    db = firestore.client()
    return db
