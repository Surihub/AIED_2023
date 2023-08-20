import streamlit as st
import pandas as pd
import requests
import plotly.express as px

def load_data(api_url):
    response = requests.get(api_url)
    data = response.json()

    return data

def main():
    st.title("OpenAPI Data Dashboard")

    st.write("Enter the OpenAPI URL:")
    api_url = st.text_input("API URL")

    if not api_url:
        st.write("Please enter a valid OpenAPI URL.")
        return

    data = load_data(api_url)

    if not data:
        st.write("Failed to load data from API.")
        return

    st.write("Sample Data:")
    st.dataframe(pd.DataFrame(data))

    st.write("Data Visualization:")
    try:
        df = pd.DataFrame(data)
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
        st.plotly_chart(fig)
    except Exception as e:
        st.write("Error: Unable to visualize the data. Please check the API response structure.")

if __name__ == "__main__":
    main()
