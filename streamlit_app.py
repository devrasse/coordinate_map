import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(layout='wide')

st.markdown('<div class="centered"><h1 style="text-align:center;"> 지도 좌표 찾기 </h1></div>', unsafe_allow_html=True)


# HTML 파일을 읽어오기
lottie_loading = load_lottiefile("lottiefiles/loading.json")
loading_state = st.empty()

with loading_state.container():
    with st.spinner('데이터 읽어오는 중...'):
        st_lottie(lottie_loading)
        with open("coordinatemap.html", "r",  encoding="utf-8") as f:
            html_code = f.read()

loading_state.empty()

with st.container(border=True,height=740):
    # Stremlit 앱에 HTML 표시
    st.components.v1.html(html_code,  height=700, scrolling=False)