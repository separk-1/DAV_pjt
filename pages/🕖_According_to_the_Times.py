import streamlit as st
import pandas as pd


# 페이지 기본 설정
st.set_page_config(
    page_icon = "🎞",
    page_title = "영화는 왜 두 시간일까❓",
    layout = "wide",
)

st.subheader("시대에 따른 영화 상영 시간 변화")

if st.button("app.py 코드 보기"):
    code = '''
    import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정
st.set_page_config(
    page_icon = "🎞",
    page_title = "영화는 왜 두 시간일까❓",
    layout = "wide",
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("영화는 왜 두 시간일까❓")
st.subheader("프로젝트 소개 👋")
    '''

use_col = ['Year', 'Runtime(Mins)', 'main_genre', 'side_genre']
df = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col)
