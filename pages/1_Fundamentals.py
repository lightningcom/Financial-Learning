import streamlit as st
import os
import importlib.util
import sys

def load_module(filepath):
    try:
        # Create a module spec
        spec = importlib.util.spec_from_file_location("dynamic_chapter", filepath)
        if spec and spec.loader:
            # Create a new module based on the spec
            module = importlib.util.module_from_spec(spec)
            # Execute the module
            spec.loader.exec_module(module)
    except Exception as e:
        st.error(f"Error loading chapter: {e}")

def fundamentals():
    with st.sidebar:
        st.page_link("Landing_Page.py", label="Back to Home", icon="🏠")
        
        # Custom CSS for "Text-Link" style buttons
        st.markdown("""
            <style>
            /* Base button style - looks like text */
            section[data-testid="stSidebar"] .stButton button {
                background-color: transparent;
                border: none;
                color: var(--text-color);
                text-align: left;
                display: block;
                width: 100%;
                padding: 0.3rem 0.5rem; /* Reduced padding */
                font-size: 10px; /* Smaller font */
                font-weight: 400;
                box-shadow: none;
                transition: background-color 0.1s, color 0.1s;
                margin: 0px;
            }

            /* Hover effect */
            section[data-testid="stSidebar"] .stButton button:hover {
                background-color: var(--background-color);
                color: var(--text-color);
                border: none;
                box-shadow: none;
                text-decoration: none;
            }

            /* Active state (simulated by disabled button) */
            section[data-testid="stSidebar"] .stButton button:disabled {
                background-color: rgba(150, 150, 150, 0.2); /* Subtle grey pill */
                color: var(--text-color);
                font-weight: 500;
                opacity: 1;
                border: none;
                border-radius: 7px;
            }
            
            /* Remove focus outline */
            section[data-testid="stSidebar"] .stButton button:focus {
                box-shadow: none;
            }

            /* Reduce spacing between buttons */
            section[data-testid="stSidebar"] .stButton {
                margin-bottom: -15px; /* Negative margin to pull them closer */
            }
            </style>
        """, unsafe_allow_html=True)
        
        st.title("Fundamental Analysis")
        
        # Define the folder path relative to the main app execution directory
        # Since we run from 'streamlit/', the folder is 'Fundamental'
        folder_path = "Fundamental"
        
        # Check if folder exists
        if not os.path.exists(folder_path):
            # Fallback for different CWD scenarios
            folder_path = os.path.join("streamlit", "Fundamental")
            if not os.path.exists(folder_path):
                 st.error(f"Could not find 'Fundamental' folder.")
                 return

        # List python files
        try:
            files = [f for f in os.listdir(folder_path) if f.endswith('.py') and f != "__init__.py"]
            files.sort() # Sort alphabetically
        except Exception as e:
            st.error(f"Error reading folder: {e}")
            return
        
        if not files:
            st.warning("No chapters found.")
            return

        # Create friendly names (remove extension)
        chapter_map = {f.replace('.py', ''): f for f in files}
        chapter_names = list(chapter_map.keys())
        
        # Initialize session state for chapter selection if not exists
        if "fund_chapter_selector" not in st.session_state:
            st.session_state.fund_chapter_selector = chapter_names[0]

        # Ensure the current selection is valid
        if st.session_state.fund_chapter_selector not in chapter_names:
             st.session_state.fund_chapter_selector = chapter_names[0]

        # Create text-like buttons for each chapter
        st.write("### Chapters")
        for chapter in chapter_names:
            if st.session_state.fund_chapter_selector == chapter:
                # Active Item
                st.button(chapter, key=f"btn_fund_{chapter}", disabled=True, use_container_width=True)
            else:
                # Inactive Item (Clickable)
                if st.button(chapter, key=f"btn_fund_{chapter}", use_container_width=True):
                    st.session_state.fund_chapter_selector = chapter
                    st.rerun()
        
        selected_chapter_name = st.session_state.fund_chapter_selector

    # Main Content
    if selected_chapter_name:
        filename = chapter_map[selected_chapter_name]
        file_path = os.path.join(folder_path, filename)
        load_module(file_path)
        
        # Navigation Buttons
        st.write("---") # Divider
        col1, col2, col3 = st.columns([1, 2, 1])
        
        current_index = chapter_names.index(selected_chapter_name)
        
        # Next Button
        if current_index < len(chapter_names) - 1:
            with col3:
                def go_to_next_chapter_fund():
                    curr_idx = chapter_names.index(st.session_state.fund_chapter_selector)
                    if curr_idx < len(chapter_names) - 1:
                        st.session_state.fund_chapter_selector = chapter_names[curr_idx + 1]
                
                st.button("Next Chapter →", on_click=go_to_next_chapter_fund)

if __name__ == "__main__":
    fundamentals()
