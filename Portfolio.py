import streamlit as st
from jinja2 import Environment, FileSystemLoader, select_autoescape
import base64
import json

template_env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

def generate_resume(user_data):
    template = template_env.get_template("PortfolioTemplate.html")
    rendered_html = template.render(data=user_data)
    return rendered_html

def save_to_html(html_content):
    with open("Portfolio.html", "w") as html_file:
        html_file.write(html_content)

def temp2(user_data=None):
    if user_data is None:
        st.title("Portfolio Generator")
        with open("user_data.json", "r") as json_file:
            user_data = json.load(json_file)
        
        st.subheader("Personal Information")
        st.write(f"Name: {user_data.get('Name', '')}")
        st.write(f"Call: {user_data.get('Call', '')}")
        st.write(f"Mail: {user_data.get('Mail', '')}")
        st.write(f"Website: {user_data.get('Website', '')}")
        st.write(f"Home: {user_data.get('Home', '')}")
        st.write(f"Twitter ID: {user_data.get('TwitterID', '')}")
        st.write(f"Linkedin ID: {user_data.get('LinkedinID', '')}")
        st.write(f"Github ID: {user_data.get('GithubID', '')}")
        st.write(f"Bio: {user_data.get('Bio', '')}")

        st.subheader("Companies")
        for company in user_data.get("Companies", []):
            st.write(f"Company Name: {company.get('CompanyName', '')}")
            st.write(f"Company Period: {company.get('CompanyPeriod', '')}")
            st.write(f"Company Role: {company.get('CompanyRole', '')}")
            st.write(f"Work Details: {company.get('WorkDetails', '')}")

        st.subheader("Education")
        for education in user_data.get("Education", []):
            st.write(f"School Name: {education.get('SchoolName', '')}")
            st.write(f"Study Period: {education.get('StudyPeriod', '')}")
            st.write(f"Course Name: {education.get('CourseName', '')}")
            st.write(f"GPA: {education.get('GPA', '')}")

        st.subheader("Projects")
        for project in user_data.get("Projects", []):
            st.write(f"Project Name: {project.get('ProjectName', '')}")
            st.write(f"Tech Stacks: {project.get('TechStacks', '')}")
            st.write(f"Project Description: {project.get('ProjectDescription', '')}")

        st.subheader("Skills")
        for skill in user_data.get("Skills", []):
            st.write(f"Skill: {skill}")

        st.subheader("Hobbies")
        for hobby in user_data.get("Hobbies", []):
            st.write(f"Hobby: {hobby}")

        st.subheader("Achievements")
        for achievement in user_data.get("Achievements", []):
            st.write(f"Achievement: {achievement}")

        st.subheader("Programming Languages")
        for pl in user_data.get("ProgrammingLanguages", []):
            st.write(f"Programming Language: {pl}")

        st.subheader("Tools")
        for tool in user_data.get("Tools", []):
            st.write(f"Tool: {tool}")

        if st.button("Generate Portfolio"):
            resume = generate_resume(user_data)
            save_to_html(resume)
            st.success("Portfolio generated successfully!")
            st.balloons()
            with open('Portfolio.html', 'rb') as f:
                st.download_button('Download portfolio', f, file_name='Portfolio.html')
    else:
        if st.button("Generate Portfolio"):
            resume = generate_resume(user_data)
            save_to_html(resume)
            st.success("Portfolio generated successfully!")
            st.balloons()
            with open('Portfolio.html', 'rb') as f:
                st.download_button('Download portfolio', f, file_name='Portfolio.html')