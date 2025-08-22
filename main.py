import streamlit as st
import folium
from streamlit_folium import st_folium
import json

# 지방 거점 국립대 매핑
regional_univs = {
    "부산광역시": "부산대학교",
    "대구광역시": "경북대학교",
    "광주광역시": "전남대학교",
    "전라북도": "전북대학교",
    "대전광역시": "충남대학교",
    "충청북도": "충북대학교",
    "강원특별자치도": "강원대학교",
    "경상남도": "경상국립대학교",
    "제주특별자치도": "제주대학교"
}

st.title("대한민국 지방 거점 국립대학 지도")

# 지도 객체 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# GeoJSON 파일 불러오기 (행정구역 경계)
# 행정구역 GeoJSON은 'korea_regions.json' 같은 파일이 필요
with open("korea_regions.json", encoding="utf-8") as f:
    geojson_data = json.load(f)

# 지역별 polygon 추가
folium.GeoJson(
    geojson_data,
    name="지역",
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["지역:"]),
    popup=folium.GeoJsonPopup(fields=["name"])
).add_to(m)

# Streamlit에서 지도 출력
map_data = st_folium(m, width=700, height=500)

# 클릭한 지역 확인
if map_data["last_active_drawing"]:
    clicked_region = map_data["last_active_drawing"]["properties"]["name"]
    st.write(f"선택한 지역: **{clicked_region}**")

    if clicked_region in regional_univs:
        st.success(f"해당 지역의 지방 거점 국립대학은 **{regional_univs[clicked_region]}** 입니다!")
    else:
        st.warning("이 지역에는 지방 거점 국립대학이 없습니다.")
