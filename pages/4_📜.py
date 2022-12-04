import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_icon = "🎞",
    page_title = "영화는 왜 두 시간일까❓",
    layout = "wide",
)

st.subheader("📜")

message = st.text_area('메세지를 입력하세요', height=3)
st.subheader(message)