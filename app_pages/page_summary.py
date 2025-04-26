import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery Mildew is a common fungal disease that affects a wide range "
        f"of plants, causing a white or gray powdery growth on the leaves.\n"
        f"* Early detection is critical, as the disease can weaken the plant, "
        f"reduce crop yields, and lead to further plant health issues.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset used in this project contains images of plant leaves "
        f"categorized as either healthy or infected with Powdery Mildew.\n"
        f"* These images were carefully curated to help train a machine learning "
        f"model to accurately classify the presence or absence of the disease."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/TafadzwaMangena/mildew-detection-in-cherry-leaves/blob/main/README.md).")


    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to visually "
        f"differentiate between healthy and unhealthy cherry leaves.\n"
        f"* 2 - The client wants to accurately predict whether a cherry leaf is "
        f"healthy or contains powdery mildew."
        )
