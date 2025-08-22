import streamlit as st
import streamlit.components.v1 as components

# 지방 거점 국립대 매핑
universities = {
    "서울특별시": "서울대학교",
    "부산광역시": "부산대학교",
    "대구광역시": "경북대학교",
    "광주광역시": "전남대학교",
    "대전광역시": "충남대학교",
    "강원도": "강원대학교",
    "경상북도": "경북대학교",
    "경상남도": "경상대학교",
    "전라북도": "전북대학교",
    "전라남도": "전남대학교",
    "충청북도": "충북대학교",
    "충청남도": "충남대학교",
    "제주특별자치도": "제주대학교",
}

# SVG 불러오기 (GitHub에서 받은 SVG 파일 내용 붙여넣거나 open()으로 읽기)
with open("skorea-provinces.svg", encoding="utf-8") as f:
    svg_map = f.read()

# SVG 안에 클릭 이벤트 추가 (자바스크립트 삽입)
svg_map = svg_map.replace(
    "<svg",
    """<svg onclick="event.stopPropagation();" 
         xmlns="http://www.w3.org/2000/svg" """)
svg_map = svg_map.replace(
    "<path ",
    """<path onclick="sendRegion(this)" style="cursor:pointer;" """
)

# JS 코드 추가
js_code = """
<script>
function sendRegion(el) {
  let region = el.getAttribute("title") || el.getAttribute("id") || "알 수 없음";
  const event = new CustomEvent("streamlit:setComponentValue", {detail: region});
  window.parent.document.dispatchEvent(event);
}
</script>
"""

region = components.html(svg_map + js_code, height=700, width=500)

# 선택된 지역 보여주기
if region and region in universities:
    st.subheader(f"📍 {region}")
    st.write(f"🎓 {universities[region]}")
elif region:
    st.subheader(f"📍 {region}")
    st.write("해당 지역에는 거점 국립대가 없습니다.")

# 클릭된 지역 처리
if region is not None and region in universities:
    st.subheader(f"📍 {region}")
    st.write(f"🎓 {universities[region]}")
