import streamlit as st
import random

# MBTI별 직업 추천 데이터 (16개)
mbti_jobs = {
    "ISTJ": ["📊 회계사", "🪖 군인", "🏛️ 행정 공무원"],
    "ISFJ": ["💉 간호사", "🤝 사회복지사", "📚 교사"],
    "INFJ": ["🧘 상담가", "✍️ 작가", "🌍 인권운동가"],
    "INTJ": ["📈 데이터 사이언티스트", "🧠 전략 컨설턴트", "🔬 연구원"],

    "ISTP": ["⚙️ 엔지니어", "✈️ 파일럿", "🚒 소방관"],
    "ISFP": ["🎨 예술가", "👗 패션 디자이너", "👐 물리치료사"],
    "INFP": ["🖋️ 작가", "💬 심리상담가", "🤲 NGO 활동가"],
    "INTP": ["📖 철학자", "💻 개발자", "🔎 연구원"],

    "ESTP": ["💼 세일즈 매니저", "🚀 기업가", "🏋️ 스포츠 코치"],
    "ESFP": ["🎤 배우", "🎉 이벤트 플래너", "🌍 여행 가이드"],
    "ENFP": ["📢 마케터", "🎙️ 강연가", "📰 언론인"],
    "ENTP": ["🏦 스타트업 창업자", "⚖️ 변호사", "🏛️ 정치인"],

    "ESTJ": ["📂 경영 관리자", "⚖️ 판사", "🪖 군 간부"],
    "ESFJ": ["👩‍⚕️ HR 매니저", "📚 초등교사", "💉 간호사"],
    "ENFJ": ["🧠 심리학자", "🏫 교육자", "🌟 정치가"],
    "ENTJ": ["💼 CEO", "⚖️ 변호사", "📊 경영 컨설턴트"]
}

# 페이지 세팅
st.set_page_config(page_title="🌈 초화려 MBTI 직업 추천 🌈", layout="wide")

# 헤더 꾸미기
st.markdown(
    """
    <div style="text-align: center; background: linear-gradient(90deg, #ff9a9e, #fad0c4, #fad0c4, #fbc2eb, #a18cd1); padding: 30px; border-radius: 15px;">
        <h1 style="color: white; font-size: 50px;">🌟 MBTI 기반 직업 추천 🌟</h1>
        <h3 style="color: #fff;">✨ 당신의 성격 유형에 꼭 맞는 직업을 찾아보세요 ✨</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# 드롭다운 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요!", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    # 랜덤한 화려한 색상 이펙트
    colors = ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1", "#F7786B", "#34AADC", "#F4A300"]
    chosen_color = random.choice(colors)

    st.markdown(
        f"""
        <div style="background-color:{chosen_color}; padding:20px; border-radius:10px; text-align:center;">
            <h2 style="color:white; font-size:30px;">🎉 당신은 <b>{selected_mbti}</b> 유형! 🎉</h2>
            <p style="color:white; font-size:18px;">어울리는 직업 리스트를 확인하세요 🔥</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"<h4 style='text-align: center;'>✨ {job} ✨</h4>", unsafe_allow_html=True)

    st.write("---")
    st.info("💡 TIP: MBTI는 성격 유형 참고용이에요! 진짜 진로는 당신의 흥미와 능력에 따라 결정하세요 🚀")
