import streamlit as st
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pdfkit
import json

# Load Jinja environment with the template folder
def temp1(user_data=None):
    template_env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    def generate_resume(user_data):
        template = template_env.get_template("ResumeTemplate.html")
        rendered_html = template.render(data=user_data)
        return rendered_html
    
    def save_to_html(html_content):
        with open("Resume.html", "w") as html_file:
            html_file.write(html_content)

    if user_data is None:
        st.title("Resume Generator")
        with open("user_data_resume.json", "r") as json_file:
            user_data = json.load(json_file)
        
        st.subheader("Personal Information")
        st.write(f"Name: {user_data.get('Name', '')}")
        st.write(f"Email: {user_data.get('Email', '')}")
        st.write(f"Phone: {user_data.get('Phone', '')}")
        st.write(f"Github ID: {user_data.get('GithubID', '')}")
        st.write(f"Linkedin ID: {user_data.get('LinkedinID', '')}")
        st.write(f"HackerRank ID: {user_data.get('HackerRankID', '')}")

        st.subheader("Institutions")
        for inst in user_data.get("Inst", []):
            st.write(f"Institution Name: {inst.get('Institutename', '')}")
            st.write(f"Degree Type: {inst.get('Degreetype', '')}")
            st.write(f"Degree Period: {inst.get('Degreeperiod', '')}")
            st.write(f"CGPA: {inst.get('cgpa', '')}")

        st.subheader("Projects")
        for project in user_data.get("Proj", []):
            st.write(f"Project Name: {project.get('ProjectName', '')}")
            st.write(f"Project Description: {project.get('ProjectDesc', '')}")
            st.write(f"Tech Stack: {project.get('ProjectStack', '')}")

        st.subheader("Achievements")
        for achievement in user_data.get("Achievement", []):
            st.write(f"Achievement: {achievement}")

        st.subheader("Programming Languages")
        for pl in user_data.get("ProgLang", []):
            st.write(f"Programming Language: {pl}")

        st.subheader("Tools")
        for tool in user_data.get("Tools", []):
            st.write(f"Tool: {tool}")

        if st.button("Generate Resume"):
            resume = generate_resume(user_data)
            save_to_html(resume)
            pdfkit.from_file("Resume.html", "Resume.pdf")
            st.success("Resume generated successfully!")
            st.balloons()
            with open('Resume.pdf', 'rb') as f:
                st.download_button('Download resume', f, file_name='Resume.pdf')
            with open('Resume.html', 'rb') as f:
                st.download_button('Download resume(HTML)', f, file_name='Resume.html')
    else:
        if st.button("Generate Resume"):
            resume = generate_resume(user_data)
            save_to_html(resume)
            pdfkit.from_file("Resume.html", "Resume.pdf")
            st.success("Resume generated successfully!")
            st.balloons()
            with open('Resume.pdf', 'rb') as f:
                st.download_button('Download resume', f, file_name='Resume.pdf')
            with open('Resume.html', 'rb') as f:
                st.download_button('Download resume(HTML)', f, file_name='Resume.html')