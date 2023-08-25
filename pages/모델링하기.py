import streamlit as st
import streamlit.components.v1 as components

st.title("Geogebra App")

# Replace this with the actual Geogebra app URL
geogebra_url = "https://www.geogebra.org/calculator"

st.write("Geogebra 계산기 사용하기")
st.components.v1.iframe(geogebra_url, height=600, scrolling=True)



st.title("Desmos API with Streamlit")

# Desmos HTML 템플릿 렌더링
with open("D:\SBH\AIED_2023\AIED_2023\pages\desmos_template.html", "r") as f:
    html_code = f.read()
components.html(html_code, width=1000, height=450, scrolling=False)

import streamlit as st
import requests

# Replace with your Wolfram Alpha API key
API_KEY = "XUET5P-R5286VWWP8"

def wolfram_alpha_query(query):
    base_url = "http://api.wolframalpha.com/v2/query"
    params = {
        "input": query,
        "format": "plaintext",
        "output": "JSON",
        "appid": API_KEY,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

st.title("Wolfram Alpha Query 사용하기")

query = st.text_input("Wolfram Alpha에게 수학 문제를 물어보세요. ")
if query:
    result = wolfram_alpha_query(query)

    if result:
        pods = result.get("queryresult", {}).get("pods", [])
        for pod in pods:
            title = pod.get("title", "")
            plaintext = pod.get("subpods", [])[0].get("plaintext", "")
            st.write(f"**{title}:** {plaintext}")
    else:
        st.error("An error occurred while querying Wolfram Alpha.")