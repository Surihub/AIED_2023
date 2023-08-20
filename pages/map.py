import streamlit as st
import plotly.express as px
import pandas as pd

def load_data():
    # Load the CSV data (change the file path accordingly)
    data = pd.read_csv("서울시_골목상권정보.csv", encoding="cp949")
    return data

def main():
    st.title("3D Graph with Seoul Street Market Data")

    data = load_data()

    # Filter rows with valid latitude and longitude values
    filtered_data = data[data["위도"].notnull() & data["경도"].notnull()]

    # Create a 3D scatter plot
    st.write("3D Scatter Plot:")
    fig = px.scatter_3d(filtered_data, x="위도", y="경도", z="총유동인구수",
                        hover_name="상권업종중분류명", color="총유동인구수",
                        labels={"총유동인구수": "Total Foot Traffic"})
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
