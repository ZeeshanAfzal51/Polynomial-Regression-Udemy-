import streamlit as st
import os

# Styling for the pages
st.set_page_config(page_title="Kalpataru Eye", page_icon="🎥", layout="wide")

# Function to display the homepage
def show_homepage():
    st.title("Welcome to Kalpataru Eye")
    st.write("""
    Welcome to **Kalpataru Eye** - The video archive showcasing the incredible projects 
    by the Kalpataru Group. Explore our extensive collection of videos from various projects.
    """)
    st.image("https://www.example.com/kalpataru_logo.png", use_column_width=True)  # Add company logo or an image
    st.markdown("---")
    st.write("**Explore our projects below or create a new project!**")

# Function to display the projects page
def show_projects_page():
    st.title("Kalpataru Projects")
    st.markdown("### Select a project to explore its videos")

    # Simulating a list of projects (this could be dynamically loaded from a database)
    projects = ["Project 1", "Project 2", "Project 3", "Project 4"]

    selected_project = st.selectbox("Choose a project", projects)

    # If a project is selected, show associated videos
    if selected_project:
        st.subheader(f"Videos for {selected_project}")
        video_options = ["Video 1", "Video 2", "Video 3"]
        selected_video = st.selectbox("Choose a video", video_options)
        if selected_video:
            st.write(f"**Playing**: {selected_video} of {selected_project}")
            st.video(f"https://www.example.com/{selected_project}_{selected_video}.mp4")  # Sample video URL

    # Option to create a new project
    st.markdown("### Create a New Project")
    with st.form(key="create_project_form"):
        new_project_name = st.text_input("Enter the new project name:")
        submit_button = st.form_submit_button("Create Project")
        if submit_button:
            st.success(f"Project '{new_project_name}' created successfully!")
            # Here, you could save the project to a database or a file

# Sidebar for navigation
def show_sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Projects"])
    return page

# Main function to handle page navigation
def main():
    page = show_sidebar()

    if page == "Home":
        show_homepage()
    elif page == "Projects":
        show_projects_page()

if __name__ == "__main__":
    main()
