import streamlit as st
from colorsys import rgb_to_hls

# -------------------------
# 1. 앱 타이틀
# -------------------------
st.markdown(
    """
    <h1 style='text-align: center; font-family: Malgun Gothic;'>전국 대학교와 학과</h1>
    """,
    unsafe_allow_html=True
)

# -------------------------
# 2. 시/도별 대학교 데이터
# -------------------------
universities = {
    "서울특별시": ["서울대학교", "연세대학교", "고려대학교", "한양대학교", "성균관대학교"],
    "광주광역시": ["전남대학교", "조선대학교", "광주과학기술원", "호남대학교", "광주대학교"],
    "부산광역시": ["부산대학교", "동아대학교", "부경대학교", "부산가톨릭대학교", "신라대학교"],
    "대구광역시": ["경북대학교", "계명대학교", "대구가톨릭대학교", "영남대학교", "경일대학교"],
    "인천광역시": ["인하대학교", "경인교육대학교", "인천대학교", "인천가톨릭대학교", "가천대학교(인천)"],
    "대전광역시": ["충남대학교", "한남대학교", "목원대학교", "배재대학교", "건양대학교"],
    "울산광역시": ["울산대학교", "을지대학교", "울산과학대학교", "동아대학교(울산)", "한국폴리텍대학(울산)"],
    "경기도": ["성균관대학교(수원)", "경기대학교", "한양대학교(ERICA)", "수원대학교", "가천대학교"],
    "강원도": ["강원대학교", "한라대학교", "강릉원주대학교", "강릉영동대학교", "연세대학교(원주)"],
    "충청북도": ["충북대학교", "청주대학교", "서원대학교", "건국대학교(충주캠)", "한국교통대학교"],
    "충청남도": ["공주대학교", "순천향대학교", "한국기술교육대학교", "호서대학교", "청운대학교"],
    "전라북도": ["전북대학교", "원광대학교", "우석대학교", "군산대학교", "전주대학교"],
    "전라남도": ["목포대학교", "순천대학교", "전남대학교(여수)", "목포해양대학교", "조선이공대학교"],
    "경상북도": ["포항공과대학교", "안동대학교", "경북대학교", "영남대학교", "대구한의대학교(경산)"],
    "경상남도": ["경상대학교", "창원대학교", "인제대학교", "마산대학교", "김해대학교"],
    "제주특별자치도": ["제주대학교", "한라대학교", "관광대학교"]
}

# -------------------------
# 3. 대학교 색상
# -------------------------
university_colors = {
    "서울대학교": "#1E4D2B","연세대학교": "#003478","고려대학교": "#A50034","한양대학교": "#004098",
    "성균관대학교": "#005BAC","전남대학교": "#008000","조선대학교": "#005BAC","광주과학기술원": "#FF6600",
    "호남대학교": "#C8102E","광주대학교": "#002F6C","부산대학교": "#004098","동아대학교": "#002F6C",
    "부경대학교": "#002F6C","부산가톨릭대학교": "#6D9BC3","신라대학교": "#C8102E","경북대학교": "#C60C30",
    "계명대학교": "#1D4E89","대구가톨릭대학교": "#2E8B57","영남대학교": "#004098","경일대학교": "#D2232A",
    "인하대학교": "#002F6C","경인교육대학교": "#1A4C8B","인천대학교": "#003DA5","인천가톨릭대학교": "#6E2639",
    "가천대학교(인천)": "#009739","충남대학교": "#005BAC","한남대학교": "#002F6C","목원대학교": "#8B1C62",
    "배재대학교": "#003478","건양대학교": "#004098","울산대학교": "#00462A","을지대학교": "#008060",
    "울산과학대학교": "#005BAC","동아대학교(울산)": "#002F6C","한국폴리텍대학(울산)": "#005BAC",
    "성균관대학교(수원)": "#005BAC","경기대학교": "#002F6C","한양대학교(ERICA)": "#004098","수원대학교": "#C8102E",
    "가천대학교": "#009739","강원대학교": "#005BAC","한라대학교": "#003478","강릉원주대학교": "#004098",
    "강릉영동대학교": "#006A4E","연세대학교(원주)": "#003478","충북대학교": "#C60C30","청주대학교": "#002F6C",
    "서원대학교": "#008060","건국대학교(충주캠)": "#006A4E","한국교통대학교": "#005BAC","공주대학교": "#004098",
    "순천향대학교": "#005BAC","한국기술교육대학교": "#0072C6","호서대학교": "#C8102E","청운대학교": "#002F6C",
    "전북대학교": "#C60C30","원광대학교": "#E03C31","우석대학교": "#004098","군산대학교": "#0072C6",
    "전주대학교": "#1D4E89","목포대학교": "#004098","순천대학교": "#008000","전남대학교(여수)": "#008000",
    "목포해양대학교": "#004098","조선이공대학교": "#005BAC","포항공과대학교": "#C8102E","안동대학교": "#002F6C",
    "경상대학교": "#006A4E","창원대학교": "#004098","인제대학교": "#0072C6","마산대학교": "#C8102E",
    "김해대학교": "#004098","제주대학교": "#006A4E","관광대학교": "#0072C6"
}

# -------------------------
# 3-1. 대학교 홈페이지
# -------------------------
university_urls = {
    "서울대학교": "https://www.snu.ac.kr/",
    "연세대학교": "https://www.yonsei.ac.kr/",
    "고려대학교": "https://www.korea.ac.kr/",
    "한양대학교": "https://www.hanyang.ac.kr/",
    "성균관대학교": "https://www.skku.edu/",
    "전남대학교": "https://www.jnu.ac.kr/",
    "조선대학교": "https://www.chosun.ac.kr/",
    "광주과학기술원": "https://www.gist.ac.kr/",
    "호남대학교": "https://www.honam.ac.kr/",
    "광주대학교": "https://www.kwangju.ac.kr/",
    "부산대학교": "https://www.pusan.ac.kr/",
    "동아대학교": "https://www.donga.ac.kr/",
    "부경대학교": "https://www.pknu.ac.kr/",
    "부산가톨릭대학교": "https://www.bcu.ac.kr/",
    "신라대학교": "https://www.silla.ac.kr/",
    "경북대학교": "https://www.knu.ac.kr/",
    "계명대학교": "https://www.keimyung.ac.kr/",
    "대구가톨릭대학교": "https://www.cu.ac.kr/",
    "영남대학교": "https://www.yu.ac.kr/",
    "경일대학교": "https://www.kyu.ac.kr/",
    "인하대학교": "https://www.inha.ac.kr/",
    "경인교육대학교": "https://www.gie.ac.kr/",
    "인천대학교": "https://www.incheon.ac.kr/",
    "인천가톨릭대학교": "https://www.icc.ac.kr/",
    "가천대학교(인천)": "https://www.gachon.ac.kr/",
    "충남대학교": "https://www.cnu.ac.kr/",
    "한남대학교": "https://www.hannam.ac.kr/",
    "목원대학교": "https://www.mokwon.ac.kr/",
    "배재대학교": "https://www.paichai.ac.kr/",
    "건양대학교": "https://www.konyang.ac.kr/",
    "울산대학교": "https://www.ulsan.ac.kr/",
    "을지대학교": "https://www.eulji.ac.kr/",
    "울산과학대학교": "https://www.usc.ac.kr/",
    "동아대학교(울산)": "https://www.donga.ac.kr/ulsan/",
    "한국폴리텍대학(울산)": "https://www.kopo.ac.kr/ulsan/",
    "성균관대학교(수원)": "https://www.skku.edu/",
    "경기대학교": "https://www.kyonggi.ac.kr/",
    "한양대학교(ERICA)": "https://www.hanyang.ac.kr/ERICA/",
    "수원대학교": "https://www.suwon.ac.kr/",
    "가천대학교": "https://www.gachon.ac.kr/",
    "강원대학교": "https://www.kangwon.ac.kr/",
    "한라대학교": "https://www.halla.ac.kr/",
    "강릉원주대학교": "https://www.gwnu.ac.kr/",
    "강릉영동대학교": "https://www.gidong.ac.kr/",
    "연세대학교(원주)": "https://www.yonsei.ac.kr/wonju/",
    "충북대학교": "https://www.chungbuk.ac.kr/",
    "청주대학교": "https://www.cju.ac.kr/",
    "서원대학교": "https://www.seowon.ac.kr/",
    "건국대학교(충주캠)": "https://www.kku.ac.kr/chungju/",
    "한국교통대학교": "https://www.ut.ac.kr/",
    "공주대학교": "https://www.kongju.ac.kr/",
    "순천향대학교": "https://www.sch.ac.kr/",
    "한국기술교육대학교": "https://www.koreatech.ac.kr/",
    "호서대학교": "https://www.hoseo.edu/",
    "청운대학교": "https://www.chungwoon.ac.kr/",
    "전북대학교": "https://www.jbnu.ac.kr/",
    "원광대학교": "https://www.wku.ac.kr/",
    "우석대학교": "https://www.useok.ac.kr/",
    "군산대학교": "https://www.kunsan.ac.kr/",
    "전주대학교": "https://www.jj.ac.kr/",
    "목포대학교": "https://www.mokpo.ac.kr/",
    "순천대학교": "https://www.scnu.ac.kr/",
    "전남대학교(여수)": "https://www.jnuy.ac.kr/",
    "목포해양대학교": "https://www.mmu.ac.kr/",
    "조선이공대학교": "https://www.cit.ac.kr/",
    "포항공과대학교": "https://www.postech.ac.kr/",
    "안동대학교": "https://www.andong.ac.kr/",
    "경상대학교": "https://www.gnu.ac.kr/",
    "창원대학교": "https://www.changwon.ac.kr/",
    "인제대학교": "https://www.inje.ac.kr/",
    "마산대학교": "https://www.masand.ac.kr/",
    "김해대학교": "https://www.kh.ac.kr/",
    "제주대학교": "https://www.jejunu.ac.kr/",
    "관광대학교": "https://www.tour.ac.kr/"
}

# -------------------------
# 4. 학과
# -------------------------
departments = {}
for city_univs in universities.values():
    for univ in city_univs:
        departments[univ] = ["컴퓨터공학과", "경영학과", "간호학과", "전기공학과", "디자인학과"]

# -------------------------
# 5. 지역 및 대학교 선택
# -------------------------
region = st.selectbox("지역을 선택하세요:", ["미선택"] + list(universities.keys()), index=0)
if region != "미선택":
    univ = st.selectbox("대학교를 선택하세요:", ["미선택"] + universities[region], index=0)
else:
    univ = "미선택"

# -------------------------
# 6. 배경 색상 적용
# -------------------------
if univ != "미선택":
    color = university_colors.get(univ, "#FFFFFF")
    r = int(color[1:3], 16)/255
    g = int(color[3:5], 16)/255
    b = int(color[5:7], 16)/255
    h, l, s = rgb_to_hls(r, g, b)
    text_color = "#FFFFFF" if l < 0.5 else "#000000"
else:
    color = "#FFFFFF"
    text_color = "#000000"

st.markdown(f"""
<style>
.stApp {{
    background-color: {color};
    color: {text_color};
    font-family: 'Malgun Gothic', sans-serif;
}}
h1, h2, h3, h4, h5, h6, .stSelectbox label {{
    color: {text_color};
}}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 7. 학과 출력 및 홈페이지 버튼
# -------------------------
if univ != "미선택":
    # 홈페이지 버튼
    if univ in university_urls:
        st.markdown(
            f"<a href='{university_urls[univ]}' target='_blank' style='text-decoration:none;'>"
            f"<button style='padding:10px 18px; border:none; border-radius:10px;"
            f"background-color: rgba(255, 255, 255, 0.6); color:{text_color}; font-weight:bold; cursor:pointer;'>"
            f"{univ} 홈페이지 바로가기</button></a>",
            unsafe_allow_html=True
        )
    
    # 학과 리스트 출력
    st.subheader(f"{univ} 학과 리스트")
    if univ in departments:
        for dept in departments[univ]:
            url = university_urls.get(univ, "#")
            st.markdown(f"- {dept}")
    else:
        st.write("학과 정보가 준비되지 않았습니다.")
