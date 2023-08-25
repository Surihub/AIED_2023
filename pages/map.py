import streamlit as st
import plotly.express as px
import pandas as pd
import requests

def load_data():
    # Seoul Street Market Information OpenAPI endpoint
    api_url = "http://openapi.seoul.go.kr:8088/YOUR_API_KEY_HERE/json/SdeTlSccoSigW/1/1000/"

    # Make a request to the API
    response = requests.get(api_url)
    data = response.json()

    # Extract relevant data from the API response
    if "SdeTlSccoSigW" in data:
        records = data["SdeTlSccoSigW"]["row"]
        df = pd.DataFrame(records)
        return df
    else:
        return None

def main():
    st.title("3D Graph with Seoul Street Market Data (OpenAPI)")

    data = load_data()

    if data is None:
        st.write("Failed to load data from API.")
        return

    # Filter rows with valid latitude and longitude values
    filtered_data = data[data["LAT"].notnull() & data["LNG"].notnull()]

    # Create a 3D scatter plot
    st.write("3D Scatter Plot:")
    fig = px.scatter_3d(filtered_data, x="LAT", y="LNG", z="INCOME_AVG",
                        hover_name="TRDAR_CD_NM", color="INCOME_AVG",
                        labels={"INCOME_AVG": "Average Income"})
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
