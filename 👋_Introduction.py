import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

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

img = Image.open('1_1.png')
st.image(img)

st.write(
    """오늘날, 영화 상영 시간은 2시간에 수렴하고 있다.\n
여기에는 다양한 이유가 있는데,
영화관은 상영횟수와 매점 회전률을 높이기 위해 짧은 러닝타임을 원하고,\n
관객은 영화 티켓 값을 지불하였기 때문에 일정 길이 이상의 러닝타임을 기대한다.\n
인간의 집중 시간과 생리 현상은 영화를 2시간 아래로 제한하였으며\n
특수효과가 많은 영화는 그만큼 메인 서사가 적어지므로 영화 길이를 길어지게 할 수 있다.\n
최근에는 OTT 서비스를 통한 긴 드라마가 인기를 얻으며 영화 길이도 전반적으로 길어지고 있다.\n
\n
영화의 초창기에는 영상을 담을 수 있는 매체가 한정적이었기 때문에 영화 길이에 많은 영향을 미쳤을 것이다.\n
본 프로젝트에서는 다음 두 주제에 대해 알아보았다.
"""
)

st.markdown("### ✅ 영화의 길이는 시대에 따라 어떻게 변화하였으며, 특히 산업적 요소와 어떠한 관계가 있을까❓")
st.markdown("### ✅ 영화의 장르는 영화 길이에 어떠한 영향을 미칠까❓")

#############
import pydeck as pdk
from urllib.error import URLError

st.subheader("🕖 영화의 길이는 시대에 따라 어떻게 변화하였을까❓")

use_col = ['Year', 'Runtime(Mins)', 'main_genre', 'side_genre']
df = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col)

st.write(
    """kaggle IMDb 5000+ Movies & Multiple Genres Dataset 을 통해 시대에 따른 영화 상영 시간 길이를 시각화하였다.
"""
)
