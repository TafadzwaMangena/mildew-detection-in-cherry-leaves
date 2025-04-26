import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    
    st.write("### Project Hypothesis and Validation")

    st.success(
    f"* The working hypothesis behind this project is that cherry leaves "
    f"affected by powdery mildew display distinct visual symptoms, most "
    f"notably the presence of white, powdery patches on the leaf surface, "
    f"which can reliably distinguish them from healthy leaves.\n\n"

    f"* To investigate this assumption, a series of visual analyses were performed:\n\n"

    f"    1. **Average Image Comparison:** Healthy leaves tend to show a clean, "
    f"uniform surface, whereas the average appearance of infected leaves clearly "
    f"displays white blotches — a visual cue associated with mildew.\n\n"

    f"    2. **Variability Image Analysis:** Infected leaves exhibit noticeable "
    f"variations, especially marked by bright streaks and irregular patterns across "
    f"the center area — patterns that are largely absent in the healthy leaf class.\n\n"

    f"    3. **Image Montage:** A side-by-side look at randomly selected healthy and "
    f"infected samples provides visual confirmation that powdery mildew typically "
    f"appears as white patches on the infected leaf surfaces."
)
