import streamlit as st
import folium
from streamlit_folium import st_folium

# ✅ 대한민국 시·도 GeoJSON 데이터 (간략화 버전)
#  → 원본은 좌표가 매우 길기 때문에 여기서는 축약된 예시만 넣었습니다.
#  실제 사용 시엔 전체 좌표를 넣으면 정상 동작합니다.
korea_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {"name": "부산광역시"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[129.0, 35.0], [129.2, 35.0], [129.2, 35.3], [129.0, 35.3], [129.0, 35.0]]]
            },
        },
        {
            "type": "Feature",
            "properties": {"name": "대구광역시"},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[[128.5, 35.7], [128.8, 35.7], [128.8, 36.0], [128.5, 36.0], [128.5, 35.7]]]
            },
        },
        # 👉 나머지 시·도들도 같은 방식으로 추가해야 전체 지도 완성됨
    ],
}

# ✅ 지방 거점 국립대 매핑
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

# ✅ 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

folium.GeoJson(
    korea_geojson,
    name="지역",
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["지역:"]),
    popup=folium.GeoJsonPopup(fields=["name"]),
).add_to(m)

# ✅ Streamlit에 지도 표시
map_data = st_folium(m, width=700, height=500)

# ✅ 클릭한 지역 처리
if map_data and map_data.get("last_active_drawing"):
    clicked_region = map_data["last_active_drawing"]["properties"]["name"]
    st.write(f"선택한 지역: **{clicked_region}**")

    if clicked_region in regional_univs:
        st.success(f"해당 지역의 지방 거점 국립대학은 **{regional_univs[clicked_region]}** 입니다!")
    else:
        st.warning("이 지역에는 지방 거점 국립대학이 없습니다.")
