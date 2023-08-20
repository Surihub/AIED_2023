import streamlit as st
import pydeck as pdk

def main():
    st.title("3D Visualization with WebGL for Education")

    st.write("Let's explore a 3D model:")
    
    # Example 3D data
    data = [
        {"position": [0, 0, 0], "color": [255, 0, 0]},
        {"position": [1, 1, 1], "color": [0, 255, 0]},
        {"position": [2, 0, 2], "color": [0, 0, 255]},
    ]
    
    # Create a PyDeck layer
    layer = pdk.Layer(
        "PointCloudLayer",
        data=data,
        get_position="position",
        get_color="color",
        get_radius=20000,
    )

    # Create a PyDeck view
    view_state = pdk.ViewState(latitude=0, longitude=0, zoom=2)

    # Create a PyDeck deck
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)

    # Render the PyDeck deck using Streamlit
    st.pydeck_chart(r)

if __name__ == "__main__":
    main()
