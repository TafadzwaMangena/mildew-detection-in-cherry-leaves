import streamlit as st


class MultiPage:
    """
    A class for managing and displaying multiple Streamlit app pages.
    """

    def __init__(self, app_name) -> None:
        """
        Create array for pages and 
        display title and favicon
        """
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️")

    def add_page(self, title, func) -> None:
        """
        Add pages to application
        """
        self.pages.append({"title": title, "function": func})

    def run(self):
        """
        Add page titles in sidebar
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu',
                                self.pages,
                                format_func=lambda page: page['title'])
        page['function']()
