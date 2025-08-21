import streamlit as st

# MBTI별 직업 추천 데이터 (16개 모두)
mbti_jobs = {
    "ISTJ": ["회계사", "군인", "행정 공무원"],
    "ISFJ": ["간호사", "사회복지사", "교사"],
    "INFJ": ["상담가", "작가", "인권운동가"],
    "INTJ": ["데이터 사이언티스트", "전략 컨설턴트", "연구원"],

    "ISTP": ["엔지니어", "파일럿", "소방관"],
    "ISFP": ["예술가", "패션 디자이너", "물리치료사"],
    "INFP": ["작가", "심리상담가", "NGO 활동가"],
    "INTP": ["철학자", "개발자", "연구원"],

    "ESTP": ["세일즈 매니저", "기업가", "스포츠 코치"],
    "ESFP": ["배우", "이벤트 플래너", "여행 가이드"],
    "ENFP": ["마케터", "강연가", "언론인"],
    "ENTP": ["스타트업 창업자", "변호사", "정치인"],

    "ESTJ": ["경영 관리자", "판사", "군 간부"],
    "ESFJ": ["HR 매니저", "초등교사", "간호사"],
    "ENFJ": ["심리학자", "교육자", "정치가"],
    "ENTJ": ["CEO", "변호사", "경영 컨설턴트"]
}

st.set_page_config(page_title="MBTI 직업 추천", layout="centered")

st.title("🌱 MBTI 기반 직업 추천 사이트")
st.write("MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# 드롭다운으로 MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

