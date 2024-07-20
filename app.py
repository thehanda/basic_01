# 以下を「app.py」に書き込み
import streamlit as st
import numpy as np
import pandas as pd

# ---------- スライダー ----------
st.title("st.slider()")
x = st.slider("xの値")
st.write(str(x) + "の4乗は" + str(x**4))

# ---------- ボタン ----------
st.title("st.button()")
if st.button("Morning?"):
    st.write("Good morinig!")
else:
    st.write("Helllo!")

# ---------- テキスト入力 ----------
st.title("st.text_input()")
st.text_input("お住まいの国", key="country")
st.session_state.country  # keyでアクセス

# ---------- チェックボックス ----------
st.title("st.checkbox()")
is_agree = st.checkbox("同意しますか？")
if is_agree:
    st.write("了解です！")
else:
    st.write("残念です！")

# ---------- セレクトボックス ----------
st.title("st.selectbox()")
df_select = pd.DataFrame({
    "col1": [11, 12, 13, 14],
    "col2": [111, 112, 113, 114]
    })
selected = st.selectbox(
    "どの番号を選びますか？",
     df_select["col2"])
st.write("あなたは" + str(selected) + "番を選びました！")

# ---------- サイドバー ----------
st.sidebar.title("st.sidebar")

y = st.sidebar.slider("yの値")
st.sidebar.write(str(y) + "の2倍は" + str(y*2))

df_side = pd.DataFrame({
    "animal": ["犬", "猫", "兎", "象", "蛙"],
    "color": ["赤", "青", "黄", "白", "黒"]
    })
selected_side = st.sidebar.selectbox(
    "どの動物を選びますか？",
    df_side["animal"]
    )
st.sidebar.write("あなたは" + str(selected_side) + "を選びました！")
