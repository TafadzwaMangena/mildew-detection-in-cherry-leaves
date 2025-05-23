import streamlit as st

from app_pages.multipage import MultiPage

# load page scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

# Create app instance
app = MultiPage(app_name="Mildew Detector")

# app pages
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaves Visualiser", page_leaves_visualizer_body)
app.add_page("Powdery Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()
