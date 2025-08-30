import streamlit as st
from colorsys import rgb_to_hls   # RGB → HLS 변환(밝기 판단용)

# -------------------------
# 1. 앱 타이틀
# -------------------------
st.markdown(
    """
    <h1 style='text-align: center; font-family: Malgun Gothic;'>전국 대학교와 학과</h1>
    """,
    unsafe_allow_html=True   # HTML 태그를 그대로 렌더링 허용
)

# -------------------------
# 2. 시/도별 대학교 데이터
# -------------------------
universities = {
    # 각 지역(키) → 해당 지역의 주요 대학교 리스트(값)
    "서울특별시": ["서울대학교", "연세대학교", "고려대학교", "한양대학교", "성균관대학교"],
    "광주광역시": ["전남대학교", "조선대학교", "광주과학기술원"],
    # ...(중략)...
    "제주특별자치도": ["제주대학교"]
}

# -------------------------
# 3. 대학교 대표 색상
# -------------------------
university_colors = {
    # 각 대학교의 대표 색상 HEX 코드 지정
    "서울대학교": "#1E4D2B",
    "연세대학교": "#003478",
    "고려대학교": "#A50034",
    # ...(중략)...
    "제주대학교": "#006A4E"
}

# -------------------------
# 4. 학과 + 이모지 데이터
# -------------------------
departments = {
    # 각 대학교 → 학과 리스트(이모지 포함)
    "서울대학교": ["컴퓨터공학과 💻", "경제학과 📈", "물리학과 🔬", "경영학과 🏢", "법학과 ⚖️"],
    "연세대학교": ["컴퓨터과학과 💻", "전자공학과 ⚡", "경영학과 🏢", "국문학과 📖", "심리학과 🧠"],
    # ...(중략)...
    "제주대학교": ["관광학과 ✈️", "해양학과 🌊", "축산학과 🐄", "간호학과 🩺"]
}

# -------------------------
# 5. 지역 및 대학교 선택
# -------------------------
# 지역 선택 드롭다운 (첫 번째 옵션은 "미선택")
region = st.selectbox("지역을 선택하세요:", ["미선택"] + list(universities.keys()), index=0)

if region != "미선택":   # 지역이 선택되면
    # 선택한 지역에 속하는 대학교 목록 출력
    univ = st.selectbox("대학교를 선택하세요:", ["미선택"] + universities[region], index=0)
else:
    univ = "미선택"       # 아무 지역도 선택 안 했을 경우

# -------------------------
# 6. 배경 색상 적용
# -------------------------
if univ != "미선택":
    st.subheader(f"{univ}의 학과 리스트")   # 선택된 대학교 제목 출력

    # 선택된 대학교 색상 HEX → RGB 변환
    color = university_colors.get(univ, "#FFFFFF")
    r = int(color[1:3], 16) / 255
    g = int(color[3:5], 16) / 255
    b = int(color[5:7], 16) / 255

    # RGB → HLS 변환 (밝기 값 l을 기준으로 글자색 결정)
    h, l, s = rgb_to_hls(r, g, b)
    text_color = "#FFFFFF" if l < 0.5 else "#000000"  # 배경이 어두우면 흰 글자, 밝으면 검은 글자
else:
    color = "#FFFFFF"     # 기본 배경 흰색
    text_color = "#000000" # 기본 글자 검정

# 선택한 배경/글자 색상 CSS 적용
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {color};   /* 전체 앱 배경 색 */
        color: {text_color};         /* 기본 글자 색 */
        font-family: 'Malgun Gothic', sans-serif;  /* 폰트 */
    }}
    h1, h2, h3, h4, h5, h6, .stSelectbox label {{
        color: {text_color};   /* 제목/라벨 색도 동기화 */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------
# 7. 학과 출력
# -------------------------
if univ != "미선택":
    if univ in departments:   # 학과 데이터가 존재하면
        for dept in departments[univ]:
            st.write(f"- {dept}")   # 학과 리스트 출력
    else:
        st.write("학과 정보가 준비되지 않았습니다.")  # 데이터 없을 경우 메시지 출력
