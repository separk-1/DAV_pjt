import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
#import streamlit_book as stb

import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('Agg')
#import seaborn as sns
import altair as alt
import plotly.express as px

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
             background-image: url("https://mblogthumb-phinf.pstatic.net/MjAxODAzMDNfMTc5/MDAxNTIwMDQxNzQwODYx.qQDg_PbRHclce0n3s-2DRePFQggeU6_0bEnxV8OY1yQg.4EZpKfKEOyW_PXOVvy7wloTrIUzb71HP8N2y-YFsBJcg.PNG.osy2201/1_%2835%ED%8D%BC%EC%84%BC%ED%8A%B8_%ED%9A%8C%EC%83%89%29_%ED%9A%8C%EC%83%89_%EB%8B%A8%EC%83%89_%EB%B0%B0%EA%B2%BD%ED%99%94%EB%A9%B4_180303.png?type=w800");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

def split_line(n):
    for i in range(n):
        st.write("\n")
    return

# text 색상
def text_64(text):
    st.markdown(f'<p style="color:#000000;font-size:64px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_32(text):
    st.markdown(f'<p style="color:#000000;font-size:32px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_24(text):
    st.markdown(f'<p style="color:#000000;font-size:24px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_18(text):
    st.markdown(f'<p style="color:#000000;font-size:18px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

def text_24_highlight(text):
    st.markdown(f'<p style="color:#0054FF;font-size:24px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

# 포맷 깔끔하게
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# header
text_64("영화는 왜 두 시간일까❓\n")
split_line(2)
text_24("""오늘날, 영화 상영 시간은 2시간에 수렴하고 있다. 여기에는 다양한 이유가 있지만, 본 프로젝트에서는 다음 두 주제에 집중하였다.\n""")
split_line(2)
text_32("✅ 영화의 길이는 시대에 따라 어떻게 변화하였으며, 그 이유는 무엇일까?\n")
split_line(2)
text_32("✅ 영화의 장르는 영화 길이에 어떠한 영향을 미쳤을까?\n")
split_line(2)
text_24("""본 프로젝트를 통해 영화 상영 시간이 2시간이 된 역사적 이유에 대하여 알아보고, 장르에 따라 달라지는 영화 상영 시간을 분석한다.""")
split_line(100)

#############
text_32("✅ 영화의 길이는 시대에 따라 어떻게 변화하였으며, 그 이유는 무엇일까?")

use_col = ['Movie_Title', 'Rating', 'Year', 'Runtime(Mins)', 'main_genre', 'side_genre']
df = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col)

st.write(
    """[Dataset](https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset?resource=download) 을 통해 시대에 따른 영화 상영 시간 길이를 시각화하였다.
"""
)

range = st.slider('아래 슬라이더를 통해 연도 범위를 조정할 수 있다.', 1920, 2022, (1920, 2022))
df_range = df[df["Year"]>=range[0]]
df_range = df_range[df_range["Year"]<=range[1]]
st.dataframe(df_range)

text_24('%s년부터 %s년까지의 영화 길이 변화는 다음과 같다.'%(range[0], range[1]))

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

#with st.expander('데이터프레임 보기') :
#    st.dataframe(Time_df)

text_24("영화는 점점 길어지고 있다!")
st.write("\n")
text_24("영화 상영 시간은 1920년대 초반은 매우 들쑥날쑥하였고, 이후 점점 증가하다 1980년대 약간 감소 후 다시 증가하고 있다.")
st.write("\n")
st.write("\n")
text_18("1900년대 초반: 필름 깡통의 용량(10-15분)")
text_18("1920년대: 필름 깡통을 이어붙이는 기술 발달, 영화의 초창기로서 상영 시간의 차이가 큼")
text_18("1940년대: TV상영 시작-TV 블록 편성을 위한 시간 제한")
text_18("1980년대: 비디오테이프의 용량 제한-120분")
text_18("1990년대: DVD 보급, 이후 인터넷 보급")
text_18("최근: OTT 서비스와의 경쟁")
st.write("\n")
st.write("\n")
text_24("영화를 전달하는 매체의 변화는 영화 상영 시간과 밀접한 관련이 있다.")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
#############
text_32("✅ 영화의 장르는 영화 길이에 어떠한 영향을 미쳤을까?")
use_col = ['Year', 'Runtime(Mins)', 'main_genre', 'side_genre']

option = st.selectbox('슬라이더 종류를 선택한다.',
                       ('10년 단위 선택', '범위 직접 조정'))
	

if option == "범위 직접 조정":
    range2 = st.slider('연도 범위를 직접 조정한다.', 1920, 2022, (1920, 2022))
    df_range2 = df[df["Year"]>=range2[0]]
    df_range2 = df_range2[df_range2["Year"]<=range2[1]]
    st.dataframe(df_range2)
    df_range_g = df_range2
    
else:
    range3 = st.slider('10년 단위로 연도를 선택한다.', 1920, 2022, 1920, 10)
    df_range3 = df[df["Year"]>=range3]
    df_range3 = df_range3[df_range3["Year"]<=range3+10]
    st.dataframe(df_range3)
    df_range_g = df_range3

Genre_list = sorted(list(set(list(df_range['main_genre']))))
Sum = []

for g in Genre_list:
    count = len(list(df_range_g[df_range_g['main_genre']==g]['main_genre']))
    Sum.append(count)

Genre_df = pd.DataFrame({"Genre": Genre_list, "Sum":Sum})

ascending_list = list(Genre_df.sort_values(by=['Sum'], axis=0, ascending=False)["Genre"][:5])

st.write(ascending_list)

fig1 = px.pie(Genre_df, values='Sum', names='Genre')      #plotly pie차트
st.plotly_chart(fig1)
 
fig2 = px.bar(Genre_df, x='Genre', y='Sum')        #plotly bar차트
st.plotly_chart(fig2)
