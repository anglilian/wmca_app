import streamlit as st
#import leafmap.foliumap as leafmap
from pages import map


def app(epc_data, sample_outputs, predicted):
    st.title("Welcome to the Demo")

    st.markdown(
        """
    Please click on tabs on the sidebar to get started
    """
    )

    map.app()
    

    