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

st.markdown("### ✅ 영화의 길이는 시대에 따라 어떻게 변화하였으며, 그 이유는 무엇일까❓")
st.markdown("### ✅ 영화의 장르는 영화 길이에 어떠한 영향을 미쳤을까❓")

#############

st.subheader("🕖 영화의 길이는 시대에 따라 어떻게 변화하였을까❓")

use_col = ['Year', 'Runtime(Mins)', 'main_genre', 'side_genre']
df = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col)

st.write(
    """[Dataset](https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset?resource=download) 을 통해 시대에 따른 영화 상영 시간 길이를 시각화하였다.
"""
)

range = st.slider('언제부터 언제까지❓', 1920, 2022, (1920, 2022))
st.text('%s년부터 %s년까지의 영화 길이 변화는 다음과 같다.'%(range[0], range[1]))

df_range = df[df["Year"]>=range[0]]
df_range = df_range[df_range["Year"]<=range[1]]

df_range['Year'] = pd.to_numeric(df_range['Year'])
year_list = sorted(list(set(list(df_range['Year']))))

Times_median = []
Times_mean = []
for y in year_list:
    times = list(df_range[df_range['Year']==y]['Runtime(Mins)'])
    Times_median.append(round(np.median(times),2))
    Times_mean.append(round(np.mean(times),2))

Time_df = pd.DataFrame({"Year": year_list, "Runtime(mean)": Times_mean, "Runtime(median)": Times_median})
Time_df = Time_df.set_index("Year")
st.line_chart(Time_df)

with st.expander('데이터프레임 보기') :
    st.dataframe(Time_df)

st.write(
    """1900년대 초반에는, 필름 깡통의 용량으로 인해 영화가 10-15분으로 무척 짧았다.\n
    1920년대에 이르러 필름 깡통을 이어붙이는 기술이 발달하며 영화는 차츰 길어졌으나, 기술의 한계로 인해 영화 길이는 지금의 절반 정도에 그쳤다.\n
    또한 영화의 초기로서 다양한 실험적인 영화들이 제작되었으며 상영 시간의 차이가 컸다.\n
    1940년대 TV상영이 시작되며 영화는 점점 길어져 앞서 서술한 바와 같이 2시간으로 수렴하였다.\n
    1980년대 비디오테이프가 등장하며 용량 관계상 1편의 영화를 테이프 하나에 전부 넣기 위해 영화는 다시 짧아졌다.\n
    1990년대에는 dvd가, 그 뒤에는 인터넷이 보급되며 영화 길이는 다시 길어졌다.\n
    더불어 70-80년대 멀티플렉스 극장의 등장으로 상영 시작시간이 전보다 중요하지 않아지고 특수효과 등 이야기 외에 다양한 볼거리가 영화에 많아지며 영화 길이는 더욱 길어졌다.\n
    최근에는 OTT 서비스와의 경쟁 또한 영화를 길어지도록 하는 것에 일조하고 있다.
"""
)
