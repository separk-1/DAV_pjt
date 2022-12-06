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

def text_32_highlight(text):
    st.markdown(f'<p style="color:#B71600;font-size:32px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)    

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
text_24("[8조] 2021-214578 건축학과 박성은")
split_line(2)
split_line(2)
split_line(2)
text_24("""오늘날, 영화 상영 시간은 2시간에 수렴하고 있다. 여기에는 다양한 이유가 있지만, 본 프로젝트에서는 다음 두 주제에 집중하였다.\n""")
split_line(2)
text_32_highlight("✅ 영화의 길이는 시대에 따라 어떻게 변화하였으며, 그 이유는 무엇일까?\n")
split_line(2)
text_32_highlight("✅ 시대에 따라 어떤 영화 장르가 인기를 끌었으며, 장르별 상영 시간에는 어떤 차이가 있을까?\n")
split_line(2)
text_32_highlight("✅ 평점과 영화 상영 시간이 관계가 있을까?\n")
split_line(2)
split_line(50)

#############
text_32("💫 영화의 길이는 시대에 따라 어떻게 변화하였을까?")

use_col = ['Movie_Title', 'Year', 'Runtime(Mins)', 'main_genre', 'side_genre']
df = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col)

st.write(
    """[Dataset](https://www.kaggle.com/datasets/rakkesharv/imdb-5000-movies-multiple-genres-dataset?resource=download) 을 통해 시대에 따른 영화 상영 시간 길이를 시각화하였다.
"""
)

range = st.slider('아래 슬라이더를 통해 연도 범위를 조정할 수 있다.', 1920, 2022, (1920, 2022))
df_range = df[df["Year"]>=range[0]]
df_range = df_range[df_range["Year"]<=range[1]]
st.dataframe(df_range)
text_18("total data Num. : %s "%(len(df_range)))

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

#with st.expander('데이터프레임 보기') :
#    st.dataframe(Time_df)

text_32("💫 그 이유는 무엇일까?")
st.write("\n")
st.write("\n")
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
text_24("영화를 전달하는 매체의 변화는 영화 상영 시간에 영향을 미쳤을 것이다.")

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
text_32("✨ 시대에 따라 어떤 장르의 영화가 인기를 끌었을까?")
st.write("\n")
st.write("\n")
use_col = ['Year', 'Runtime(Mins)', 'main_genre', 'side_genre']

option = st.selectbox('슬라이더 종류를 선택한다.',
                       ('10년 단위 선택', '범위 직접 조정'))
	

if option == "범위 직접 조정":
    range2 = st.slider('연도 범위를 직접 조정한다.', 1920, 2022, (1920, 2022))
    df_range2 = df[df["Year"]>=range2[0]]
    df_range2 = df_range2[df_range2["Year"]<=range2[1]]
    df_range_g = df_range2
    
else:
    range3 = st.slider('10년 단위로 연도를 선택한다.', 1920, 2022, 1920, 10)
    df_range3 = df[df["Year"]>=range3]
    df_range3 = df_range3[df_range3["Year"]<=range3+10]
    df_range_g = df_range3

st.dataframe(df_range_g)
text_18("total data Num. : %s "%(len(df_range_g)))
st.write("\n")
st.write("\n")
Genre_list = sorted(list(set(list(df['main_genre']))))
Sum = []

for g in Genre_list:
    count = len(list(df_range_g[df_range_g['main_genre']==g]['main_genre']))
    Sum.append(count)

Genre_df = pd.DataFrame({"Genre": Genre_list, "Sum":Sum})

st.write("\n")
st.write("\n")

text_24("TOP 3 Genre")
ascending_list = list(Genre_df.sort_values(by=['Sum'], axis=0, ascending=False)["Genre"][:3])
ascending_df = pd.DataFrame({"Rank": [1, 2, 3], "Genre": ascending_list})
st.dataframe(ascending_df)

text_24("WORST 3 Genre")
descending_list = list(Genre_df.sort_values(by=['Sum'], axis=0, ascending=True)["Genre"][:3])
descending_df = pd.DataFrame({"Rank": [1, 2, 3], "Genre": descending_list})
st.dataframe(descending_df)

Genre_df = Genre_df.sort_values(by=['Sum'], axis=0, ascending=False)
fig1 = px.pie(Genre_df, values='Sum', names='Genre', template="ggplot2")      #plotly pie차트
fig1.update_layout(plot_bgcolor="black", font = {'color':'white'})
st.plotly_chart(fig1)
 
fig2 = px.bar(Genre_df, x='Genre', y='Sum', template="ggplot2")        #plotly bar차트
fig2.update_layout(plot_bgcolor="black", font = {'color':'white'})
st.plotly_chart(fig2)
st.write("\n")
st.write("\n")
text_18("1950년대까지: 드라마, 코미디 장르 인기")
text_18("1960년대부터: 액션 장르 인기 끌기 시작")
text_18("2010년대부터: 액션 장르가 1위를 차지")
st.write("\n")
st.write("\n")
text_24("시대에 따라 주로 제작되는 영화 장르는 차이가 있으며 영화 초기 드라마와 코미디 장르가 인기를 끌던 것에서, 최근들어 액션 장르가 인기가 있다.")
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

text_32("✨ 장르별 상영 시간에는 어떠한 차이가 있을까?")
st.write("\n")
st.write("\n")

range4 = st.slider('연도 범위를 조정한다.', 1920, 2022, (1920, 2022))
df_range4 = df[df["Year"]>=range4[0]]
df_range4 = df_range4[df_range4["Year"]<=range4[1]]

text_24('%s년부터 %s년까지의 장르별 영화 상영 시간은 다음과 같다.'%(range4[0], range4[1]))

option = st.selectbox('영화 길이 변수를 선택한다.',
                       ('평균', '중위수'))

Times_median = []
Times_mean = []


for g in Genre_list:
    times = list(df_range4[df_range4['main_genre']==g]['Runtime(Mins)'])
    Times_median.append(round(np.median(times),2))
    Times_mean.append(round(np.mean(times),2))

if option=="평균":
    Time = Times_mean
else:
    Time = Times_median


Genre_df2 = pd.DataFrame({"Genre": Genre_list, "Time":Time})
Genre_df2 = Genre_df2.sort_values(by=['Time'], axis=0, ascending=False)
 
fig3 = px.bar(Genre_df2, x='Genre', y='Time', template="ggplot2")        #plotly bar차트
fig3.update_layout(plot_bgcolor="black", font = {'color':'white'})
st.plotly_chart(fig3)
text_18("전체 평균으로는, 뮤지컬 장르가 평균 216분, 애니메이션 장르는 평균 93분으로 차이가 있었다.")
text_18("1920-1950년까지는 드라마 장르가 111분으로 가장 길었고, 호러영화가 73분으로 가장 짧았다.")
text_18("이후 1980년까지는 전기, 서부영화, 어드벤쳐 장르가 140분대로 가장 길었으며 애니메이션, 호러 영화가 가장 짧았다.")
text_18("80년대부터 현재까지는 새로 등장한 뮤지컬 영화가 압도적으로 길었으며 애니메이션, 호러 영화는 여전히 가장 짧은 순위를 차지하였다.")

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
text_32("🎬 영화 평점과 상영시간과의 관계")
st.write("\n")
st.write("\n")
text_24("최근 영화 시간이 길어지는 이유 중 하나가, 긴 영화가 오스카 등 유명 영화제 수상에 유리하기 때문이라는 견해가 있다.")
text_24("이를 확인하기 위하여 영화 상영시간과 평점의 관계를 산점도로 표현하였다.")
text_18("수상 여부만을 기준으로 분석하기에는 오래된 영화에 대한 데이터가 없고 영화제별 기준이 달라 평론가의 평점을 기준으로 분석하였다.")
st.write("\n")
st.write("\n")

use_col2 = ['Movie_Title', 'Year', 'Rating', 'Runtime(Mins)', 'main_genre', 'side_genre']
df2 = pd.read_csv("./IMDb_All_Genres_etf_clean1.csv", usecols = use_col2)

option = st.selectbox('슬라이더 종류 선택',
                       ('10년 단위', '직접 조정'))
	

if option == "직접 조정":
    range5 = st.slider('직접 조정', 1920, 2022, (1920, 2022))
    df_range5 = df2[df2["Year"]>=range5[0]]
    df_range5 = df_range5[df_range5["Year"]<=range5[1]]
    df_range5 = df2[df2["Year"]>=range5[0]]
    df_range5 = df_range5[df_range5["Year"]<=range5[1]]
    df_scatter = df_range5
    st.write("\n")
    st.write("\n")
    text_24('%s년부터 %s년까지의 영화 평점과 상영시간과의 관계는 다음과 같다.'%(range5[0], range5[1]))
    
else:
    range6 = st.slider('10년 단위', 1920, 2022, 1920, 10)
    df_range6 = df2[df2["Year"]>=range6]
    df_range6 = df_range6[df_range6["Year"]<=range6+10]
    df_scatter = df_range6
    st.write("\n")
    st.write("\n")
    text_24('%s년부터 %s년까지의 영화 평점과 상영시간과의 관계는 다음과 같다. 데이터의 색상은 영화의 장르를 나타낸다.'%(range6, range6+10))

st.dataframe(df_scatter)
text_18("total data Num. : %s "%(len(df_scatter)))

chart = alt.Chart(df_scatter).mark_circle().encode( x = 'Runtime(Mins)', y='Rating', color = 'main_genre' )   ##알테어 
st.altair_chart(chart, use_container_width=True)
text_24("영화 상영 시간은 평점에는 큰 영향을 미치지 않는다.")

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
text_32("🎄 결론")
st.write("\n")
st.write("\n")
text_24("본 프로젝트를 통해 영화의 상영 시간이 시대에 따라 증가해 왔으며, 영향을 전달하는 매체의 변화가 이에 영향을 미쳤을 것으로 확인할 수 있었다.")
text_24("또한, 시대에 따라 인기있는 영화 장르와 장르별 상영 시간 차이를 분석하였다.")
text_24("마지막으로 영화 평점과 상영시간의 관계에 대해 알아보았다.")
st.write("\n")
st.write("\n")
text_24("본 프로젝트의 아쉬운 점은 데이터가 특정 연도에 편중되어 있어 정확한 분석이 어려웠다는 것이다. 더 많은 데이터를 통해 시각화뿐만 아니라 회귀분석까지 진행한다면 보다 정량적인 결과를 얻을 수 있을 것이다.")