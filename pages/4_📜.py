import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_icon = "🎞",
    page_title = "영화는 왜 두 시간일까❓",
    layout = "wide",
)

st.subheader("📜")

name = st.text_input('이름을 입력하세요!')
if name != '' :
    st.subheader(name + '님 안녕하세요??')

message = st.text_area('메세지를 입력하세요', height=3)

st.subheader(message)