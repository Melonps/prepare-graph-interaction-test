import datetime

import streamlit as st

name = st.text_input("名前を入力してください")
date = st.date_input("日付を入力してください")
time = st.time_input("時間を入力してください", datetime.time(13, 00))

st.write(
    f"""件名:   「グラフの読み上げの実験」参加のためのZoomミーティング参加情報

{name}様、


お世話になっております。大阪公立大学大学院情報学研究科の筧です。
この度は、私たちのグラフの読み上げの実験にご参加いただきありがとうございます。実験参加のためのZoomミーティングの詳細を以下に記載いたします。

日時: {date} {time}

ミーティングURL
https://omu-ac-jp.zoom.us/j/7373217365?pwd=bXNwRjd5VDZzV1VyNjdNYVBVNTM2Zz09
ミーティングID
737 321 7365
パスコード
984767

お時間になりましたら、上記のURLにアクセスし、ミーティングIDとパスコードを入力してください。
実験中はZoomの画面共有機能と、録画機能を使用させていただく場合がございます。ご了承ください。

何かご質問やご不明点がございましたら、お気軽にご連絡ください。


大阪公立大学大学院情報学研究科
筧万里"""
)
