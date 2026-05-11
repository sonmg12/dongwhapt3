import streamlit as st

st.title("🛠 충전기/포장기 에러 가이드")

# 에러 데이터를 간단하게 저장 (나중에 더 늘릴 수 있습니다)
error_db = {
    "0892": {"name": "No Leaflet", "solution": "리플렛 매거진 보충 및 흡착컵 청소", "img": "https://via.placeholder.com/400x300?text=Check+Leaflet"},
    "0521": {"name": "Temp Error", "solution": "히터 선 연결 상태 및 설정 온도 확인", "img": "https://via.placeholder.com/400x300?text=Check+Heater"}
}

code = st.text_input("에러 번호를 입력하세요:")

if code in error_db:
    st.header(f"⚠️ {error_db[code]['name']}")
    st.subheader("✅ 해결 방법")
    st.write(error_db[code]['solution'])
    st.image(error_db[code]['img']) # 사진이 나오는 부분
elif code:
    st.error("등록되지 않은 에러 번호입니다.")