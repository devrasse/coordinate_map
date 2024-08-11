import streamlit as st

st.set_page_config(layout='wide')
# HTML 파일을 읽어오기
with open("coordinatemap.html", "r",  encoding="utf-8") as f:
    html_code = f.read()

st.markdown('<div class="centered"><h1 style="text-align:center;"> 지도 좌표 찾기 </h1></div>', unsafe_allow_html=True)

with st.container(border=True,height=740):
    # Stremlit 앱에 HTML 표시
    st.components.v1.html(html_code,  height=700, scrolling=False)