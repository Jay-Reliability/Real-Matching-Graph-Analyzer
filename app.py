import os
import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 설정 (와이드 모드, 패딩 최소화)
st.set_page_config(
    page_title="실사용매칭시험 데이터 Analyzer V2.0",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Streamlit 기본 헤더/푸터 및 여백 제거 CSS 주입
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        div.block-container {
            padding: 0rem 0rem 0rem 0rem !important;
            margin: 0rem 0rem 0rem 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            width: 100% !important;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. HTML 파일 로드 함수
@st.cache_data(show_spinner=False)
def load_analyzer_html():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(current_dir, "02_Matching_Test_Graph_Web_Analyzer.html")
    
    if not os.path.exists(html_path):
        st.error(f"❌ '{html_path}' 파일을 찾을 수 없습니다. 동일한 디렉토리에 배치되었는지 확인해 주세요.")
        st.stop()
        
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# 4. 컴포넌트 렌더링
html_code = load_analyzer_html()
components.html(html_code, height=940, scrolling=True)