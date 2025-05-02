import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    """
    Display Project Hypothesis Page information
    """
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* The working hypothesis behind this project is that cherry leaves "
        f"affected by powdery mildew display distinct visual symptoms, most "
        f"notably the presence of white, powdery patches on the leaf surface, "
        f"which can reliably distinguish them from healthy leaves.\n\n"

        f"* To investigate this assumption, a series of visual analyses"
        f"were performed:\n\n"

        f"    1. **Average Image Comparison:** Healthy leaves tend to show a "
        f"clean, uniform surface, whereas the average appearance of infected "
        f"leaves clearly displays white blotches — a visual cue associated "
        f"with mildew.\n\n"

        f"    2. **Variability Image Analysis:** Infected leaves exhibit "
        f"noticeable variations, especially marked by bright streaks and "
        f"irregular patterns across the center area — patterns that are "
        f"largely absent in the healthy leaf class.\n\n"

        f"    3. **Image Montage:** A side-by-side look at randomly selected "
        f"healthy and infected samples provides visual confirmation that "
        f"powdery mildew typically appears as white patches on the infected "
        f"leaf surfaces."
    )
