import streamlit as st

# 시/도별 대학교 리스트
universities = {
    "서울특별시": ["서울대학교", "연세대학교", "고려대학교"],
    "광주광역시": ["전남대학교", "조선대학교", "광주과학기술원"],
    "부산광역시": ["부산대학교", "동아대학교", "부경대학교"],
    "대구광역시": ["경북대학교", "계명대학교", "대구가톨릭대학교"],
    "인천광역시": ["인하대학교", "경인교육대학교", "인천대학교"],
    # 필요한 지역 추가
}

st.title("지역별 대학교 리스트")

# 사용자가 선택할 수 있는 드롭다운
selected_region = st.selectbox("지역을 선택하세요", list(universities.keys()))

# 선택된 지역의 대학교 리스트 표시
if selected_region:
    st.subheader(f"{selected_region}의 대학교")
    for uni in universities[selected_region]:
        st.write(f"- {uni}")
