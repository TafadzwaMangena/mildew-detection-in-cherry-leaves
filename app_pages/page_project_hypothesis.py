import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* The working hypothesis behind this project is that cherry leaves affected "
        f"y powdery mildew display distinct visual symptoms, most notably the presence of white, "
        f"powdery patches on the leaf surface, which can reliably distinguish them from healthy leaves. \n\n"
        f"* To investigate this assumption, a series of visual analyses were performed: "
        f"1. The Average Image Comparison highlights that healthy leaves tend to show a clean, uniform surface, whereas the average appearance of infected leaves clearly displays white blotches — a visual cue associated with mildew. "
        f"The Variability Image Analysis indicates that infected leaves exhibit noticeable variations, especially marked by bright streaks and irregular patterns across the center area — patterns that are largely absent in the healthy leaf class."
        f"The Image Montage offers a side-by-side look at randomly selected healthy and infected samples, providing visual confirmation that powdery mildew typically appears as white patches on the infected leaf surfaces."

    )