import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit_book as stb

# 페이지 이름
st.set_page_config(
    page_icon = "📽",
    page_title = "영화는 왜 두 시간일까❓",
    layout = "wide",
)

# 배경 이미지 설정
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/7991231/pexels-photo-7991231.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

# 포맷 깔끔하게
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# header
st.header("영화는 왜 두 시간일까❓")

st.success(
    """오늘날, 영화 상영 시간은 2시간에 수렴하고 있다.\n
여기에는 다양한 이유가 있지만,
본 프로젝트에서는 다음 두 주제에 집중하였다.
"""
)

st.markdown("### ✅ 영화의 길이는 시대에 따라 어떻게 변화하였으며, 그 이유는 무엇일까❓")
st.markdown("### ✅ 영화의 장르는 영화 길이에 어떠한 영향을 미쳤을까❓")

#############

st.subheader("🕖 영화의 길이는 시대에 따라 어떻게 변화하였을까❓")

use_col = ['Year', 'Runtime(Mins)', 'main_genre', 'side_genre']
df = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col)

st.success(
    """[Dataset](https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset?resource=download) 을 통해 시대에 따른 영화 상영 시간 길이를 시각화하였다.
"""
)

range = st.slider('언제부터 언제까지❓', 1920, 2022, (1920, 2022))
st.success('%s년부터 %s년까지의 영화 길이 변화는 다음과 같다.'%(range[0], range[1]))

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

st.success(
    """
    1900년대 초반에는, 필름 깡통의 용량으로 인해 영화가 10-15분으로 무척 짧았다.\n
    1920년대에 이르러 필름 깡통을 이어붙이는 기술이 발달하며 영화는 차츰 길어졌으나, 기술의 한계로 인해 영화 길이는 지금의 절반 정도에 그쳤다.\n
    또한 영화의 초기로서 다양한 실험적인 영화들이 제작되었으며 상영 시간의 차이가 컸다.\n
    1940년대 TV상영이 시작되며 영화는 점점 길어져 앞서 서술한 바와 같이 2시간으로 수렴하였다.\n
    1980년대 비디오테이프가 등장하며 용량 관계상 1편의 영화를 테이프 하나에 전부 넣기 위해 영화는 다시 짧아졌다.\n
    1990년대에는 dvd가, 그 뒤에는 인터넷이 보급되며 영화 길이는 다시 길어졌다.\n
    더불어 70-80년대 멀티플렉스 극장의 등장으로 상영 시작시간이 전보다 중요하지 않아지고 특수효과 등 이야기 외에 다양한 볼거리가 영화에 많아지며 영화 길이는 더욱 길어졌다.\n
    최근에는 OTT 서비스와의 경쟁 또한 영화를 길어지도록 하는 것에 일조하고 있다.
"""
)
