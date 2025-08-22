import streamlit as st
import streamlit.components.v1 as components

# 지방 거점 국립대 데이터
universities = {
    "서울": "서울대학교",
    "부산": "부산대학교",
    "대구": "경북대학교",
    "광주": "전남대학교",
    "대전": "충남대학교",
    "강원": "강원대학교",
    "경북": "경북대학교",
    "경남": "경상대학교",
    "전북": "전북대학교",
    "전남": "전남대학교",
    "충북": "충북대학교",
    "충남": "충남대학교",
    "제주": "제주대학교",
}

# 선택한 지역 (세션에 저장)
if "selected_region" not in st.session_state:
    st.session_state["selected_region"] = None

# SVG 예시 (실제로는 훨씬 큰 SVG가 필요합니다)
svg_map = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 500" width="300">
  <style>
    .region { fill: lightgray; stroke: black; stroke-width: 1; cursor: pointer; }
    .region:hover { fill: orange; }
  </style>
  <script>
    function selectRegion(region) {
      const streamlitEvent = new CustomEvent("streamlit:setComponentValue", {detail: region});
      window.parent.document.dispatchEvent(streamlitEvent);
    }
  </script>
  <rect x="50" y="50" width="100" height="100" class="region" onclick="selectRegion('서울')" />
  <rect x="200" y="100" width="120" height="120" class="region" onclick="selectRegion('부산')" />
  <rect x="100" y="250" width="150" height="150" class="region" onclick="selectRegion('대구')" />
</svg>
"""

region = components.html(svg_map, height=600, width=500)

# 클릭된 지역 처리
if region is not None and region in universities:
    st.subheader(f"📍 {region}")
    st.write(f"🎓 {universities[region]}")
