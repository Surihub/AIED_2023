import streamlit as st

st.title("Geogebra App")

# Replace this with the actual Geogebra app URL
geogebra_url = "https://www.geogebra.org/calculator"

st.write("Geogebra 계산기 사용하기")
st.components.v1.iframe(geogebra_url, height=600, scrolling=True)
